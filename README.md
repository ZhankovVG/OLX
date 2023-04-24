<p align="center">
      <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/OLX_2019.svg/1200px-OLX_2019.svg.png" width="300" height="100">
</p>

<p align="center">
   <img src="https://img.shields.io/badge/Django%20-4.1.3-green">
   <img src="https://img.shields.io/badge/django--allauth-0.52.0-orange">
   <img src="https://img.shields.io/badge/License-MIT-yellow">
</p>

## About the project

In this project, I tried to reproduce the OLX site. Implemented various transitions, category selection and product selection from the category. Implemented registration and adding a new ad. As well as a hidden phone number, which you can see by clicking on it and contacting the seller. I would ask you not to criticize much for the fact that the site is not highly optimized in the future I will try to fix it.
## Documentation

Description of routes:

- "Empty path, ProductView.as_view() is named main. This is the main page of my web application."<br>
- "'create/': The path that renders the view CreateProductView.as_view() and is named create_post. This is the page for creating a new product in your web application."<br>
- "'datail/<slug:slug>/': A path that contains the <slug:slug> parameter and passes it to the ProductDatailView.as_view() view. The slug parameter is used to display the details of a specific product, and this route is named datail."<br>
- "'search/': A path that maps to the SearchView.as_view() view and is named search. This is the product search page in your web application."<br>
- " 'category/<slug:slug>/': A path that contains the <slug:slug> parameter, passing it to the CategoryView.as_view(). The slug parameter is used to display the products of a particular category, and this route is named category."<br>
- " 'comments/<int:pk>/': A path that contains the <int:pk> parameter, passing it to the CommentsView.as_view() view. The pk parameter is used to display comments for a particular product, and this route is named comments."

Description View:

- " CategoryOutput - class responsible for outputting categories. It contains the get_context_data method, which adds all objects of the Category model to the data context, and passes it on with a call to super().get_context_data(*args, **kwargs). "<br>
- " ProductView - class responsible for displaying products. It inherits the CategoryOutput class and the ListView class from Django, and defines a Product model for working with data. It also defines a queryset attribute that contains the Product.objects.filter(draft=False) filter to get only published products. "<br>
- " ProductDatailView - a class responsible for the full description of the product. It inherits the DetailView class from Django and defines a Product model for working with data. It also defines a slug_field attribute of 'url' to search for a product by the url field. "<br>
- " SearchView - a class responsible for searching for products on the site. It inherits the CategoryOutput class and the ListView class from Django, and defines a Product model for working with data. It also defines a get_queryset method that filters products by the title field containing the substring obtained from the search parameter in the GET request. "<br>
- " CategoryView - a class responsible for displaying products by category. It inherits the CategoryOutput class and the ListView class from Django, and defines a Product model for working with data. It also defines the template_name attribute, which contains the name of the template to render, and the get_queryset method, which filters the products by the category obtained from the slug URL parameter. "<br>
- " CreateProductView - the class responsible for adding a new ad. It inherits from Django's View class, and defines get and post methods to process GET and POST requests, respectively. The get method returns the AddNewPostForm form, and the post method saves the data from the form, creates a new Product object with the form, saves it, and redirects to the main page. "<br>
- " CommentsView - class responsible for adding a comment to a product. It inherits the View class from Django, and defines a post method to handle the POST request. The post method receives data from the AddComentsForm, finds the corresponding product by its id, creates a new comment using the form, saves it, and redirects to the product page. "<br>


## Developers

- [Vitaliy Zhankov] (https://github.com/ZhankovVG)

## P.S. Thank you for reading and visiting my repository, have a nice day!
