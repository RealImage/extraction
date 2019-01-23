'use strict';

const util = require('util');
const fs = require('fs');
const simpleParser = require('mailparser').simpleParser;
var mailattach = []

// mailattch = [{ filename: '', content: '' }, {  }]
// regex to get email address inside the brackets <>. 
// Because mail.email returns email: 'Hello world! <helloworld@gmail.com>'

var regExp = /\<([^)]+)\>/;

module.exports = function mailparser(data){
    return new Promise(function(resolve, reject){
        simpleParser(data)
            .then(mail => {
                for (var attach in mail.attachments){
                mailattach.push({
                    attachment : mail.attachments[attach],
                    date : mail.date,
                    email : regExp.exec(mail.from.text)[1]
                });
            }
            resolve(mailattach);
            })
            .catch(err => {
                console.log("parse err",err);
                reject(err);
                
        });
    })
}
