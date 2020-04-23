# [App Demo](https://csc301-nagraha3-perei345-a1.herokuapp.com/actor.html)

# docker
Instead of running all the docker comands below, we can use a [Makefile](Makefile).

To rebuild the container with your changes:

`make reload`

To start:

`docker build -t a1-301 .`

`docker run -d --name a1-301-container -p 80:80 a1-301:latest`

`docker start a1-301-container`

To stop/remove container:

`docker stop a1-301-container`

`docker rm a1-301-container`

# heroku
`heroku login`

`heroku create --app <app-server-name>`

`heroku container:login`

`heroku container:push web --app <app-server-name>`

`heroku container:release web --app <app-server-name>`

`heroku open --app <app-server-name>`


# Objective Statement
Providing a platform to the Directors and Actors of a theatric performance to help them implement the blocking of their script and remove data ambiguity during this process, therefore, making the communication and coordination among them easier.

# Personas
<!--
reference: https://qubstudio.com/blog/4-examples-of-ux-personas/
-->
<details>
  <summary>Bob (Actor 1)</summary>
 
  - Occupation - Actor 
  - Demographics
    - (age - 26, location - Toronto, marital status - single)
  - Goals - Performing in a theater (Learning the script, positioning and acting)
  - Needs - Script
  - Personality 
    - Tech Savy, Active, and Enthusiatic.

</details>

<details>
  <summary>Sophie (Actor 2)</summary>
 
  - Occupation - Full time Accountant, Part time Actor 
  - Demographics
    - (age - 34, location - Toronto, marital status - single)
  - Goals - Working as a full time Accountant and taking out time for Acting in her busy schedule (Learning the script, positioning and acting)
  - Needs - Script and Time management
  - Personality 
    - Tech Savy, Active, and Ambitious

</details>

<details>
  <summary> Alice (Director 1)</summary>

  - Occupation - Director of Theatric Performances
  - Demographics 
    - (age - 41, location - Toronto, marital status - married)
  - Goals - Incharge of directing theateric performances (deciding the roles and placement of the Actors in a performance)
  - Needs - Actors, Script and Stage
  - Personality 
    - Luddite, Hard working, and Serious.

</details>


# User Stories
<!--
reference: https://www.atlassian.com/agile/project-management/user-stories
-->

1. As a Director, I want to be able to view the blocking of any script for all actors, so that I can instruct and coordinate during rehearsals. 

1. As a director, I want to be able to modify the blocking of any part of the script, so that I can decide on and edit the placement of any of the actors based on the requirements of the script easily. 

1. As an Actor, I want to be able to view my blocking for all my lines in the script, so that I can check my position for every line of the script during the play and save time.


# Acceptance Criteria
<!--
Conditions that a product must satisfy to be accepted by the user in the user story
-->

1. The blocking of the script requested by the director should be displayed.
1. The director should be able to modify the blocking of the script.
1. The director should be able to save the modified script.
1. The product should be able to display all the blockings for a particular actor using the script and actor number. 



# JSON files 

### [script_get_data.json](app/script_get_data.json)
This JSON object is the response from a GET request to the `/script/<script id>` endpoint. The API is made to be generic so that as the UI changes and new features are needed, it should remain backwards compatible. The parent object has two keys, `scripts` and `actors`.

The `scripts` value is an array. This is to follow RESTful practices which would support requesting a single resource or muliple when making a GET request to `/script`. The script objects contain the script number, the script text (`text`), and an array of  blockings (`blocking`). 

These blocking items are objects which include a part number (`part`), the start and end index of the script text and an array of positions (`positions`). The position objects contain the stage position and the actor name and their id.

### [script_post_data.json](app/script_post_data.json)
The JSON contains two major details - `scriptNum` and `parts`.

`scriptNum` stores the number of the script and parts contains all the parts of the script in an array. 

`parts` further containes detailed information such as the part number (`part`) and the blocking (`blocking`) as an array of every actor and their position in that part. 

Using this structure simplifies accessing the script we need to edit using `scriptNum` and further comparing the details of all the parts of the script by traversing through the `parts` array. The `parts` array compares actor name and position in each part to the existing record.