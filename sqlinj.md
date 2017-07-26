# SQL Injection

## MS-SQL Functions and Variables

Name | Params | Description
-----|--------|------------
SUBSTRING | | 
ASCII | | 
LEN | | 
@@VERSION | | 
DB_NAME() | | 


## Column inferring in UNION

**DBs:** MS-SQL, Oracle

When infering column number for MS-SQL/Oracle use `..NULL,NULL..` not `..1,2,3..` for column values cause you hit type checking.

## Enclose SELECTs in braces

**DBs**: MS-SQL

When you have a statement of the kind `SELECT col1 FROM tbl1 WHERE ... LIMIT 1`, in order to use the result in `LEN()` or `SUBSTRING()`
you have to enclose the SELECT in braces:

    WHERE 'M'=SUBSTRING((SELECT TOP 1 NAME FROM sysobjects), 1,1) --
    WHERE 15=LEN((SELECT TOP 1 NAME FROM sysobjects)) --

### References

* [Testbed for queries](http://sqlfiddle.com)
* [MSSQL Practical Injection Cheat Sheet](https://www.perspectiverisk.com/mssql-practical-injection-cheat-sheet/)
* [MSSQL SQL Injection Cheat Sheet](http://www.sqlinjectionwiki.com/categories/1/mssql-sql-injection-cheat-sheet/)
* [MSSQL Injection Cheat Sheet](http://pentestmonkey.net/cheat-sheet/sql-injection/mssql-sql-injection-cheat-sheet)
* [MS Reference](https://docs.microsoft.com/en-us/sql/index)
* [MSDN Tutorial](https://msdn.microsoft.com/en-us/library/ms189826(v=sql.90).aspx)