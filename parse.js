'use strict';

const util = require('util');
const fs = require('fs');
const simpleParser = require('mailparser').simpleParser;
var mailattach = []

// regex to get email address from string 
// Because mail.email returns email: 'Hello world! <helloworld@gmail.com>'

var regExp = /([a-zA-Z0-9+._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)/;

module.exports = function mailparser(data){
    return new Promise(function(resolve, reject){
        simpleParser(data)
            .then(mail => {
                console.log(mail.from.text)
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
                console.log("parse error :",err);
                reject(err);              
        });
    })
}
