// dependencies
var async = require('async');
var AWS = require('aws-sdk');
var mailparse = require('./parse.js');
// get reference to S3 client 
var s3 = new AWS.S3();
var util = require('util');


exports.handler = function (event, context, callback) {
    // Read options from the event.
    var eventBody = event.Records[0].body;
    console.log("event :", event)
    sourceS3 = JSON.parse(eventBody).Records[0].s3;
    var srcBucket = sourceS3.bucket.name;
    // Object key may have spaces or unicode non-ASCII characters.
    var srcKey = decodeURIComponent(sourceS3.object.key);
    srcKey = srcKey.replace(/\+/g,' ');
    var dstBucket = process.env.S3_BUCKET;
    var dstKey = srcKey;

    console.log("Name of the blob : ", srcKey)

    // Sanity check: validate that source and destination are different buckets.
    if (srcBucket == dstBucket) {
        callback("Source and destination buckets are the same.");
        return;
    }

    //async waterdall docs https://caolan.github.io/async/docs.html#waterfall
    async.waterfall([
        function download(next) {
            // Download the file from S3 into a buffer.
            console.log("Downloading file from source")
            s3.getObject({
                Bucket: srcBucket,
                Key: srcKey
            },
                next); //refer docs to understand this 
        },
 
        function parse(response, next) {
            console.log("Attempting to parse attachments")
            data = response.Body;
            mailparse(data).then(mailparse => {
                contentType = response.ContentType;
                next(null, mailparse)
            }).catch((err) => {
                console.log(err)
                callback("error parsing attachments.")
            });
        },

        function upload(mailattachments, next) {
            // Stream the transformed file to a different S3 bucket.
            if(mailattachments.length==0){
                throw "There are no attachments present!!";
            }
            console.log("Uploading to destination bucket")
            Promise.all(mailattachments.map((mailattachment) => {
                return new Promise((resolve, reject) => {
                    s3.putObject({
                        Bucket: dstBucket,
                        Key: mailattachment.email + '/' + mailattachment.date.toISOString() + '/' + mailattachment.attachment.checksum + '/' + mailattachment.attachment.filename.toString('base64'),
                        Body: mailattachment.attachment.content,
                        ContentType: contentType
                    }, (err, data) => {
                        if (err) {
                            console.log("here :", err)
                            reject(err)
                        } else {
                            resolve(data)
                        }
                    })
                })
            })).then(() => next()).catch(next)
        }], function (err) {
            if (err) {
                console.error(
                    'Unable to download ' + srcBucket + '/' + srcKey +
                    ' and upload to ' + dstBucket + '/' + dstKey +
                    ' due to an error: ' + err
                );
            } else {
                console.log(
                    'Successfully downloaded ' + srcBucket + '/' + srcKey +
                    ' and uploaded to ' + dstBucket + '/' + dstKey
                );
            }

            callback(null, "Successfull");
        }
    );
};
