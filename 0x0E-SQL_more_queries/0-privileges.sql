-- Lists all privileges of the MySQL users user_0d_1 and user_0d_2
SELECT
    user,
    host,
    privilege_type
FROM
    mysql.user
JOIN
    mysql.db
ON
    mysql.user.user = mysql.db.user
WHERE
    (user = 'user_0d_1' OR user = 'user_0d_2')
    AND host = 'localhost';
