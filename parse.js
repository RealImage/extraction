'use strict';

const util = require('util');
const fs = require('fs');
const simpleParser = require('mailparser').simpleParser;
var mailattach = {
    filename: [],
    content: []
}

// mailattch = [{ filename: '', content: '' }, {  }]

module.exports = function mailparser(data){
    return new Promise(function(resolve, reject){
        simpleParser(data)
            .then(mail => {
            resolve(mail.attachments);
            })
            .catch(err => {
                console.log("parse err",err);
                reject(err);
                
        });
    })
}
