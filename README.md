# BOOKWORM

Bookworm is an online book store where users can look for books based on the book genre. 

Deployed at: https://milestone-project-4-ana.herokuapp.com/

## UX

The store is designed to enable users to register, login and logout for data protection services. 

They can also see their order history and choose the "remember information" option, in order not to have to fill out their personal info at every purchase. 

Users can search for books based on genre (fiction and nonfiction), which is easily accessible at the top of the page.

The navigation bar also allows entails a search bar, which allows the user to search the store by a certain name or word. 


#### User Stories

As a user, I want:

- to have my data protected
- to have an easy access to my previous orders
- to search for books by category / genre


#### Wireframes

As there are many pages to this project, I have included the wireframes in a separate document.

Please see the wireframes.md file for the entire collection of wireframes:

https://github.com/AMikic33/milestone-project-4/tree/master/static/wireframes

## Features

#### Existing Features

- Login - The customers are able to create their own accounts and log into the website with secure details.
- Sign-Up - New users can sign up themselves if they wish to set up an account.
- User Profile - Each user has their own profile.
- Users can view their order history from their profile
- Users can log out at any time from the store by clicking on the logout button
- Users can add items to the cart while browsing the store, from there they can remove the items or 
    checkout using the Stripe payment management system securely and easily
- Users can search on the products page for items based on name so that they can narrow down their options
- Users can choose their country from a pick list to avoid spelling errors

##### Staff users

- Create data - Staff users can add new products to the database using a simple form.
- Eidt data - Staff users can edit existing products to the database using a simple form.
- Delete data - Staff users can delete existing products by simply klicking delete button.

#### Features left to be implemented

- Users will be able to create a wishlist which will notify them if the wished product is in the store
- Product reviews will be created


## Technologies used

- HTML - This site uses HTML to instruct the browser how to interprit the code correctly and arrange the layout.
- CSS - This site uses CSS to aid in the style, and overall theme of the website
- Bootstrap - This site uses Bootstrap elements to help design the framework of the site
- Django - This was the chosen framework for developing the project
- Python - This language was chosen to code the a large amount of the functionality of the site
- JavaScript - this was used to program some of the features on the site, such as the calendar
- Balsamiq - This was used to create the wireframes in the design phase
- Heroku - This was chosen to host the website app for deployment.
- Stripe - This was used to process the credit card payments in the checkout app
- Amazon AWS - S3 Buckets were set up and used for storing website images and files
- Postgres - This Relational Datatabase was used to handle the data storage


## Testing

##### User Credentials

There are two main uses on this site; a site member and a site staff member. 
Please use the login below on the following link:

https://milestone-project-4-ana.herokuapp.com/admin/login/?next=/admin/

username: testname
email: test@test.com
password: testytest


#### Bugs found

- user is able to insert their details when registering, but the email verification does not get sent 
- user is able to insert their username and password to login, but the login is not possible due to the lack of the verifcation email
- user is not able to open orders in profile/ order history
- success and error pop-up messages can not be closed


## Deployment

This project was deployed to Heroku at the address https://milestone-project-4-ana.herokuapp.com/ using the following steps

###### GitHub:

- Create a new project on GitHub
- Copy the code for pushing to a GitHub repository and paste in the terminal of your project on GitPod (git remote add origin 'link')
- To commit the code on GitPod to GitHub:
- In the terminal, type "git add ." to add all new changes to the code to staging area
- Commit these by typing "git commit -m" and adding a detailed description of the commit in ""
- Next, push the code commit to GitHub by typing "git push"

##### Heroku:

- Create a Heroku account
- Create a new app
- Link the Heroku app with your GitHub repository
- Push changes to git using the terminal and verify that the connection to Heroku is working
- Add environment variables to Heroku settings.


## Credits

#### Content

- cover photo: https://drama.uktv.co.uk/period-drama/article/20-classic-books-you-have-read-you-die/
- noimage.jpeg: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.entrepreneur.com%2Fslideshow%2F343776&psig=AOvVaw1ubV-AaVisynkwWTVqMj4Y&ust=1612125237545000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCJj7jOXAxO4CFQAAAAAdAAAAABAL

- Book description and photo : "Crime and Punishment": https://en.wikipedia.org/wiki/Crime_and_Punishment
- Book description and photo : "The Daughter of Time": https://en.wikipedia.org/wiki/The_Daughter_of_Time
- Book description and photo : "Romeo and Juliet": https://en.wikipedia.org/wiki/Romeo_and_Juliet
- Book description and photo : "The Shining": https://en.wikipedia.org/wiki/The_Shining_(novel)
- Book description and photo : "Murder on the Orient Express": https://en.wikipedia.org/wiki/Murder_on_the_Orient_Express
- Book description and photo : "I Am Malala": https://en.wikipedia.org/wiki/I_Am_Malala
- Book description and photo : "Encyclopædia Britannica": https://en.wikipedia.org/wiki/Encyclop%C3%A6dia_Britannica
- Book description and photo : "The Lessons of History": https://en.wikipedia.org/wiki/The_Lessons_of_History
- Book description and photo : "Thus Spoke Zarathustra":  https://en.wikipedia.org/wiki/Thus_Spoke_Zarathustra
- Book description and photo : "A Brief History of Time": https://en.wikipedia.org/wiki/A_Brief_History_of_Time
- Book description and photo : "Into the Wild": https://en.wikipedia.org/wiki/Into_the_Wild_(book)

- relying on the lessons from the mini project Boutique-Ado and using the code from the lessons. 


#### Acknowledgements

- I would like to acknowledge my mentor Reuben Ferrante, for all the help and support on this project.
- I would like to thank the Code Insitute Tutor's for all of their help. 
    In particular, Scott and Igor, who have been a massive help.
- I would also like to thank my friends and family for all of their support.