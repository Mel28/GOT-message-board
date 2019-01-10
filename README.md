<h1>Game of thrones message board season 9</h1>
<h3> The following steps were taken to build this application</h3>
<ul>
<li> Installed Flask framework using 'sudo pip3 install Flask'</li>
<li> Import Flask, os, render_template, redirect </li>
<li> created requirements.txt file using 'pip3 freeze --local > requirements.txt'</li>
<li> Added ability to write to and read from a list and display the chat items</li>
<li> Added timestamp and user.txt file</li>
<li> refactor views to use HTML templates and handle post requests from the user form.</li>
<li> Added chat.html, updated so that message board is updated every 5000 milliseconds</li>
<li> Created messages.txt file so messages on message board are saved and can be seen next time</li>
you load the chat.
<li> Used start bootstrap clean blog theme, downloaded files and added link to head of html</li>
<li> adapted bootstrap theme for my own use</li>
<li> App should be responsive and adapt to fit all devices</li>
<li> Created Heroku app and pushed to heroku master</li>
<li> Created Procfile by entering 'echo web: python app.py > Procfile'</li>
<li> Set scale with 'heroku ps:scale web=1' command</li>
<li> Added config variables in heroku settings</li>
<li> Deployed application successfully to Heroku: https://got-season9-discussion-board.herokuapp.com/ </li>