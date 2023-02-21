# Email Transition Application

## Purpose

I created this project to easily send out generated emails to users with their new login information. This is being used ahead of a transition from one email provider to Microsoft Exchange hosted in the cloud.

## Tools I used

I used [MJML](https://github.com/mjmlio/mjml) to create a responsive email template and then used Python to loop through a CSV file to send out the credentials with the template.

## Installation instructions for development

Once you've cloned the repo you need two things: MJML and the Python implementation of dotenv.

I've opted to install MJML globally with `npm i -g mjml` which allows me to use the CLI.

To use [python-dotenv](https://pypi.org/project/python-dotenv/) run `pip install python-dotenv`.

Once you have everything installed create a `.env` file to place the `NOREPLY_PASS` environment variable in and you should be good to go.

To build the email template use `npm run build`, you can also have it watch the `.mjml` file for changes and auto-generate with `npm run watch`.

## End review

I originally tried to code the email template by hand, until I realized that every email client implements their own HTML/CSS parsing (let's not even talk about Microsoft Outlook not supporting `border-radius` in 2023). This is exactly what transpilers were made for, and MJML was good enough for what I needed.

If I needed to code a responsive email template in the future, I'll probably use a different framework. I ran into 2 issues while throwing this together that weren't _massively_ detrimental but still annoyed me. The first was a bug where if you have too many `mj-text` elements (it almost seemed arbitrary) in a column a random border or gap will appear. The other issue was not being able to group elements together in anything besides a column/section. Wrappers exist for sections, and groups for columns - but I needed something to group `mj-text` elements, have the individual text elements align to the left, but the container itself to the center. This can't be done as far as I can tell.

All-in-all, it will get the job done, and it wasn't too hard to build.
