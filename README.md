# BLOG-IT
A personal blogging website where you can create and share your opinions and other users can read and comment on them.

## Built by [EUGENE NZIOKI](https://github.com/EugeneZnm)

## User Requirements

 1. As a user, I would like to view the blog posts submitted
 2. As a user, I would like to comment on blog posts
 3. As a user, I would like to view the most recent posts
 4. As a user, I would like to alerted when a new post is made by joining a subscription.
 5. As a writer, I would like to sign in to the blog.
 6. As a writer, I would also like to create a blog from the application.
 7. As a writer, I would like to delete comments that I find insulting or degrading.
 8. As a writer, I would like to update or delete blogs I have created.

## Features

  + [x] Your project should have a functioning authentication system
  + [x] In your models, implement at least 1 one-many relationship.
  + [x] Your project should have a user model.
  + [x] Your project should have a comment model.
  + [x] Your project should have a profile page
  + [ ] Your project should implement Ajax functionality.

## Installation

### Requirements
This project was created on a debian linux platform but should work on other unix based[not limited to] sytems.

* Tested on Debian Linux
* Python 3.6.4

## Cloning of the respository
   * In terminal:
   
    $ git clone https://github.com/EugeneZnm/BLOG-IT.git
    
## Creating the Virtual Environment

    sudo apt-get install python3.6-venv
    python3.6 -m venv virtual
    source virtual/bin/activate

## Install Dependencies

    pip3 install -r requirements.txt
    
## Required Libraries     
   * Flask==0.12.2
   * Flask-Bootstrap4==4.0.2
   * Flask-Script==2.0.6
   * gunicorn==19.7.1
   
## Running Tests

    python3.6 manage.py test
    
## Running the web app 
    python3.6 manage.py server
   
   open app in browser by default on 127.0.0.1:5000

## Live Demo

This web app can be accessed from the following link:

    https://codexznm.herokuapp.com/ 
    
## Quick Start

    usage: manage.py [-?] {server,test,shell,runserver} ...

    positional arguments:
      {server,test,shell,runserver}
        server              Runs the Flask development server i.e. app.run()
        test                Run the unit tests.
        shell               Runs a Python shell inside Flask application context.
        runserver           Runs the Flask development server i.e. app.run()
    
    optional arguments:
      -?, --help            show this help message and exit
      
## Technology Used

   * Python3.6
   * Flask   
   * Heroku
   
## License Information

   MIT License

Copyright(c) 2018

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
