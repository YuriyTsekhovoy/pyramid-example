**README.md**

This is a simple Pyramid application that demonstrates how to filter data from a SQLite database.

**Usage**

To start the application, run the following command:

```
python app.py
```

This will start a web server on port 6543. You can then access the application in your web browser at `http://localhost:6543`.

To filter data from the database, simply enter the table name, column name, and value to filter on in the URL path, like this:

```
http://localhost:6543/{table}/{column}/{value}
```

For example, to filter the `Artist` table by the `Name` column with the value `AC/DC`, you would enter the following URL:

```
http://localhost:6543/Track/Composer/AC/DC
```

The application will then return a list of all rows in the `Track` table where the `Composer` column is equal to `AC/DC`.

**Table information**

The application also displays information about the table that you are filtering. This information includes the column names and data types.

**Error handling**

If you enter an incorrect table name or column name, the application will return an error message. The error message will also include instructions on how to fix the problem.

**Dependencies**

This application requires the following Python libraries:

* Pyramid
* SQLAlchemy
* Mako
* Pyramid Debug Toolbar

**License**

This application is licensed under the MIT License.