# MyLibrary

MyLibrary is a backend system which takes care of all the books you have and want to read. This app ass I said is 
more like a backend system related with a restapi (the django rest framework api) where the design UI/UX is not that
important. From here the simplistic design: 


![Website main page](MyLibrary-documentation/frontend-image-one.jpg)

Even tough the design considerations are not that important in this case, I still believe
the app should possess a responsive design, so I implemented the app in that manner.

![Website main page](MyLibrary-documentation/responsive-frontend-design.jpg)

## Backend

In the backend I have 7 models, each of them being strongly related to one another.

* Authors -> which includes all the authors from the library
* Book Types -> which includes all types of books that the library possess
* Books -> which includes the actual books from the library
* Current reading books -> which includes the books that you're currently reading
* Done to read books -> which includes the books that you already read.
* To read books -> which includes the books that you need to read
* Wishlist -> which includes the books that you want in your library

##### Authors

##### BookTypes

##### Books

##### CurrentReadingBooks

##### DoneToReadBooks

##### ToReadBooks

##### Wishlist