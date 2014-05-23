meta-documents
==============

document rappresentation using metaprogramming in python

This simple project explain how metaprogramming can help developers to write reusable and elegant code.
You can do the same things writing less code using metaprogramming.

This is a sample of endpoint implementation to create some entity like a document
and retrieve it using his id.

The same endpoints are implemented using inheritance (bill, receipt, document microapp)
and metaprogramming (meta_bill, meta_receipt and finally doc_meta_app that use a single
definition for three endpoints)



Requirements
============

Django==1.6.1

djangorestframework==2.3.12

