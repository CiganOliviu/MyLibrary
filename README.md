# MyLibrary

MyLibrary is a backend system which takes care of all the books you have and want to read. This app ass I said is 
more like a backend system related with a restapi (the django rest framework api) where the design UI/UX is not that
important. From here the simplistic design: 


![Website main page](MyLibrary-documentation/frontend-image-one.JPG)

Even tough the design considerations are not that important in this case, I still believe
the app should possess a responsive design, so I implemented the app in that manner.

![Website main page](MyLibrary-documentation/responsive-frontend-design.JPG)

## Backend

In the backend I have 7 models, each of them being strongly related to one another.

* Authors -> which includes all the authors from the library
* Book Types -> which includes all types of books that the library possess
* Books -> which includes the actual books from the library
* Current reading books -> which includes the books that you're currently reading
* Done to read books -> which includes the books that you already read.
* To read books -> which includes the books that you need to read
* Wishlist -> which includes the books that you want in your library

The models can be seen below

![Website main page](MyLibrary-documentation/backend-models.JPG)

##### Authors

The authors table represents a simple registration of all the authors from the library. In this way, 
the reader can  be aware of the most preferred authors, or what every author has written. 
From the administration system you can actualise, change or add new authors very easy through 
a basic form.

![Website main page](MyLibrary-documentation/admin-sys-authors.JPG)

This table is linked to other models like Books, CurrentReadingBooks, DoneToReadBooks etc. by a foreign key.
Each book has an author, and the author must me registered in the system. 

Like every table from this system, this one is integrated along the django rest api framework.

![Website main page](MyLibrary-documentation/restapi-authors.JPG)

The data can be accessed in raw json format as well.

![Website main page](MyLibrary-documentation/raw-restapi-authors.JPG)

##### BookTypes

This table consists in information about books types. It is directly linked by a foreign key with all the tables
from this database in one way or another, except the Authors table. Having such a table is extremely important 
because in this way you as a reader can categorize and filter books with much more ease, not only by the author.

From the administration system you can actualise, change or add new types of books very easy through 
a basic form.

![Website main page](MyLibrary-documentation/admin-sys-bookstypes.JPG)

Note the interesting level field. With that one, you can adjust your interests so that you can get relevant books
recommendations or just categorize your books by the interesting level.



##### Books

##### CurrentReadingBooks

##### DoneToReadBooks

##### ToReadBooks

##### Wishlist