# <p style="text-align: center;"><span style="font-family: Times New Roman; font-size: 3em;"> Databases </span>

###### <p style= "text-align: center ; "> Databases fact finding exercise. </span>

<p align="center"> <img src="https://res.cloudinary.com/practicaldev/image/fetch/s--VrozJ74G--/c_imagga_scale,f_auto,fl_progressive,h_420,q_66,w_1000/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/o2vhujyw4y75sz2zemi8.gif" alt="drawing" width="1000" height="500"/> </p>



#### <span style="color:#FF5733">1. What is the difference between a relational and a non-relational database?  </span>
- Relational Database:

> - Organizes data in tables with rows and columns.
> - Has a fixed, structured schema.
> - Uses SQL (Structured Query Language) for queries.
> - Suitable for structured data with well-defined relationships.

- Non-Relational Database (NoSQL):

> - Stores data in various formats, like key-value, document, or graph.
> - Has a flexible or dynamic schema.
> - Uses various query languages tailored to the specific data model.
> - Ideal for unstructured or semi-structured data and agile development.

####  <span style="color:#FF5733">2. What are indexes? </span>

>Indexes in a database are like the table of contents in a book. They help the database find and retrieve data faster by providing a roadmap to where specific information is located.

> - Indexes are data structures that store a subset of the data's columns in a highly efficient, searchable format.
> - They make database queries faster by allowing the database to quickly pinpoint the rows that meet certain criteria.
> - Think of an index as an organized list that helps you find information in a large database table without having to read the whole thing.

> In a nutshell, indexes help databases find data faster, like a book's table of contents helps you find a specific topic without reading the entire book.


#### <span style="color:#FF5733">3. What are primary keys and secondary keys?</span>

>Primary Keys and Secondary Keys are like unique IDs for database records, helping the database organize and retrieve information. Here's a simple explanation:

- Primary Key:

> - Acts as a unique identifier for each record in a database table.
> - Guarantees that each record has a distinct and unchanging key.
> - Used for linking and referencing data between tables.

- Secondary Key:

> - Also known as a "Non-Primary Key."
> - Helps in searching and organizing data but is not required to be unique.
> - Used for optimizing query performance and data retrieval.

> In essence, a Primary Key is like a fingerprint, ensuring each record is unique, while Secondary Keys are like tags that help organize and speed up data retrieval.

#### <span style="color:#FF5733">4. What are inner joins and outer joins?</span>

- Inner Join:

> - Think of it as a filter for matching information.
> - Combines data from two tables, showing only the matching rows.
> - If a row in one table has no match in the other, it's excluded from the result.

- Outer Join:

> - Think of it as a way to see everything, including what doesn't match.
> - Combines data from two tables, showing both matching and non-matching rows.
> - Useful for seeing all data, even when there are no matches in one of the tables.

> In simple terms, an Inner Join shows only what matches, while an Outer Join shows everything, including what doesn't match.

#### <span style="color:#FF5733">5. What is the difference between DROP TABLE and TRUNCATE TABLE?</span>

- DROP TABLE:

> - It's like deleting the entire table from the database.
> - Removes the table structure and all its data.
> - Cannot be undone, and you need to recreate the table from scratch.

- TRUNCATE TABLE:

> - It's like emptying a table while keeping the structure.
> - Deletes all the data but leaves the table intact.
> - Can be faster and less resource-intensive than DROP TABLE.


> In simple terms, DROP TABLE wipes out the table completely, while TRUNCATE TABLE clears the data but preserves the table structure for future use.


#### <span style="color:#FF5733">6. What are the different data types in SQL? </span>

> - INTEGER: For whole numbers, like 1, 42, or -5.
> - VARCHAR(N): For text or strings, where N is the maximum length.
> - DATE: For dates, like '2023-11-02'.
> - FLOAT/DOUBLE: For decimal numbers with or without precision.
> - BOOLEAN: For true or false values.
> - CHAR(N): For fixed-length character strings.
> - BLOB: For binary data like images or documents.
> - TIMESTAMP: For date and time combined, like '2023-11-02 14:30:00'.


#### <span style="color:#FF5733">7. What are the WHERE and HAVING clauses used for?</span>

- WHERE Clause:
> The WHERE clause is used to filter records based on a specified condition. It is used with the SELECT, UPDATE, and DELETE statements.

> - Think of it as a filter for rows in a table.
> - Used with SELECT, UPDATE, or DELETE statements.
> - Filters rows based on specified conditions, like "age > 30."

- HAVING Clause:
> The HAVING clause is used to filter the results of an aggregate function in a GROUP BY query. It is applied after the GROUP BY clause and can filter groups based on conditions involving aggregate functions.

> - Think of it as a filter for groups of data.
> - Used with GROUP BY in SQL.
> - Filters groups (resulting from grouping data) based on conditions, like "average salary > 50000."

>In simple terms, WHERE filters individual rows, while HAVING filters groups of data after they've been grouped.

<p align="center"> <img src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2016/11/AWS-Feature.png" alt="drawing" width="800" height="600"/> </p>

<p style="text-align: center;"><span style="font-family: Times New Roman; color:#FF5733"> Room 3 - Tanumatiben . Khalid . Hani . Moritala . Isra . Beewong </span>

<p align="center"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/SNice.svg/640px-SNice.svg.png" width="200" height="200"/> </p>



