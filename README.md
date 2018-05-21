# TO RUN THE APPLICATION
 - To run the application you have to have vagrant and virtual box installed on your machine.
 - Then clone the repository from https://github.com/udacity/fullstack-nanodegree-vm.
 - Then you need to download the newsdata.sql file from https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip,and put it in the vagrant directory.
 - Now open bash in the vagrant directory and then you need to run the command vagarnt up and vagrant ssh.
 - Now To load the data, use the command psql -d news -f newsdata.sql.
 - Using the cd command get inside the newsdata folder in bash.
 - Then you just need to run the news.py file on your machine.
# WORKING OF THE APPLICATION
 - The application simply shows the output of some sql queries.
 - The first query displays the most popular 3 articles of all time.
 - The second query displays the most popular authors of all time.
 - The third query displays the day when more than 1 % of requsts lead to error.
# VIEWS CREATED
### FOR QUESTION 1
1. create view log_output as select replace(path,'/article/','') AS article,count(path) from log group by path order by count(path) desc;
### For Question 2
1. create view log_output as select replace(path,'/article/','') AS article,count(path) from log group by path order by count(path) desc;(This is the same view used for question 1)
2. create view articles_log as select articles.author,sum(log_output.count) from log_output inner join articles on log_output.article=articles.slug group by articles.author order by articles.author;
### FOR QUESTION 3
1. create view total_stat as select count(status),date(time) from log group by date(time) order by date(time);
2. create view err_stat as select count(status),date(time) from log where status LIKE ('%404 NOT FOUND') group by date(time) order by date(time);
3. create view results as select err_stat.date,ROUND((err_stat.count*100.0/total_stat.count),4) AS error from err_stat inner join total_stat on err_stat.date=total_stat.date;

