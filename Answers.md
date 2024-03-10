1. Explain the relationship between the "Product" and "Product_Category" entities from the above diagram.

Ans. In the database schema diagram you provided, the "Product" and "Product_Category" entities are through a foreign key relationship. Here's how they connected:

    -> The "Product" entity has an attribute named category_id which is a foreign key.

    -> This cateogry_id references the primary key id in the "Product_Category" entity.

    -> This means that ecach product is linked to a specific category, indicationg what type of product it is.

This relationship allows the database to maintain referential integrity between products and their categories, ensuring that all products are assigned to a vaild category. It also enables efficient queries to retrieve all products within a particular category.

2. How could you ensure that each product in the "Product" table has a valid category assigned to it?

Ans. To ensure that each product in the "Product" table has a valid category assigned to it, it can implement the following measures:

    -> Referntial Integrity Constraints: Use foregin key constraints in database schema. This will enforce the relationship between the Product_Category tables, ensuring that every category_id in the Product_Category table.

    -> Database Triggers: Create triggers that check for the existence of the category before inserting or updating records in tha Product table.

    -> Application Logic: Implement validation checks within your application's business logic to ensure that products are only created with existing and vaild categories.

    Data Quality Checks: Regularly run data quality checks or audits to find and correct any products that may have invalid category assignements.

By combining these methods, it can maintain the integrity of your product-category relationships in the database.

