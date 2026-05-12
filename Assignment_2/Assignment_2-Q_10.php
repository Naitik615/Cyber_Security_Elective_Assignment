<?php

$db = new SQLite3("testdb.db");

$db->exec("CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)");

$db->exec("INSERT INTO users (username, password)
VALUES ('admin', '1234')");

echo "Enter username: ";
$user = trim(fgets(STDIN));

echo "Enter password: ";
$pass = trim(fgets(STDIN));

$stmt = $db->prepare("SELECT * FROM users WHERE username = :user AND password = :pass");

$stmt->bindValue(':user', $user, SQLITE3_TEXT);
$stmt->bindValue(':pass', $pass, SQLITE3_TEXT);

$result = $stmt->execute();

$row = $result->fetchArray();

if ($row) {
    echo "Login Successful\n";
} else {
    echo "Invalid Credentials\n";
}

?>
