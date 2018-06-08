# Odoo Technical Training


Odoo Technical Training on v11


Learning Outcome
================
 * Understand the development concepts and architecture
 * Develop a new Odoo module
 * Integrate any third-party tool of Odoo

Contributors
------------

 * Tosin Komolafe <hello@tosinkomolafe.com>


Outline
=======
 * Introduction & History of Odoo
 * Technical Fundamentals of Odoo Addons
 * Inheritance
 * ORM Methods
 * Introduction to Different Types of Button and Overview of Linked Views
 * Creating and Demonstrating Data and Sequence
 * Wizard
 * Web Services
 * Odoo Server Parameters and Configuration
 * Security in Odoo
 * Designing Analytical (BI) View
 * Workflow
 * Reporting



Many2many options
=================
For a many2many field, a list of tuples is expected. Here is the list of tuple that are accepted, with the corresponding semantics:
 * (0, 0, { values }) link to a new record that needs to be created with the given values dictionary
 * (1, ID, { values }) update the linked record with id = ID (write values on it)
 * (2, ID) remove and delete the linked record with id = ID (calls unlink on ID, that will delete the object completely, and the link to it as well)
 * (3, ID) cut the link to the linked record with id = ID (delete the relationship between the two objects but does not delete the target object itself)
 * (4, ID) link to existing record with id = ID (adds a relationship)
 * (5) unlink all (like using (3,ID) for all linked records)
 * (6, 0, [IDs]) replace the list of linked IDs (like using (5) then (4,ID) for each ID in the list of IDs)


 External Links
===============
 * https://www.odoo.com/documentation/8.0/api_integration.html