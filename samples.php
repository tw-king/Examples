<!DOCTYPE html>
<html>
	<head>
		<title>PHP samples</title>
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta charset="UTF-8">
		<link rel="stylesheet" href="/css/base.css">
		<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
		<link rel="stylesheet" href="https://www.w3schools.com/lib/w3-colors-flat.css">
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
		<!-- Global site tag (gtag.js) - Google Analytics -->
		<script async src="https://www.googletagmanager.com/gtag/js?id=UA-117249412-1"></script>
		<script src="/js/common.js"></script>
		<style>
			.left-algn {
				text-align: left;
			}
		</style>
	</head>
	<?php
		// Add comment field variables
		$email = $text =  "";
		
		// Database queries
		$qry_Comments = "Select * from examples.comments Order by entry_dt desc";
		$qry_GenBkAuth = "SELECT books.title, genre.genre, concat(authors.surname, ', ', authors.firstnames) as author "
			. "FROM examples.book_genre "
			. "Left Outer Join examples.books on books.id = book_genre.book_id "
			. "Left Outer Join examples.genre on genre.id = book_genre.genre_id "
			. "Left Outer Join examples.authors on authors.id = books.author_id "
			. "Order by genre.genre, books.title";
		$qry_LangBkAuth = "SELECT books.title, languages.language, concat(authors.surname, ', ', authors.firstnames) as author "
			. "FROM examples.book_lang "
			. "Left Outer Join examples.books on books.id = book_lang.book_id "
			. "Left Outer Join examples.languages on languages.id = book_lang.language_id "
			. "Left Outer Join examples.authors on authors.id = books.author_id "
			. "Order by languages.language, books.title";
	?>
	<body class="w3-flat-silver">
		<div class="w3-container w3-flat-silver">
			<div class="w3-cell-row w3-padding-24">
				<div class="w3-cell w3-cell-middle s3 m3 l3">
					<div class="w3-hide-large">
						<button class="w3-button w3-blue w3-large" onclick="w3_open_common()">&#9776;</button>
					</div>
					<div class="w3-sidebar w3-top w3-bar-block w3-collapse w3-flat-silver w3-card" style="width:165px;" id="common-nav">
						<a href="/index.html" class="nav-but w3-bar-item w3-button">Home</a>
						<button class="nav-but w3-bar-item w3-button" onclick="openexample('db1')">Add comments<br><sup>db Record creation</sup></button>
						<button class="nav-but w3-bar-item w3-button" onclick="openexample('db2')">View comments<br><sup>db SQL Select</sup></button>
						<button class="nav-but w3-bar-item w3-button" onclick="openexample('db3')">Books by genre<br><sup>db SQL Select Join</sup></button>
						<button class="nav-but w3-bar-item w3-button" onclick="openexample('db4')">Bks by language<br><sup>No data example</sup></button>
					</div>
				 </div>

				<div class="w3-col s9 m9 l9 w3-round-xlarge w3-blue w3-animate-left w3-right w3-margin-right">
					<h1 class="w3-center w3-hide-small">PHP Samples</h1>
					<h1 class="w3-center w3-hide-medium w3-hide-large">PHP</h1>
				</div>
			</div>
			
			<div id='common' class="w3-main" style="padding-left: 10px; margin-left:175px">
				<div id="db1" class="w3-panel example">
					<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
						<h3>Leave a comment</h3>
						<label>Email</label><input name="your_email" class="w3-input w3-hover-light-grey" type="email" size=60>
						<label>Comment</label>
						<textarea name="your_text" class="w3-input w3-hover-light-grey" rows="10"></textarea>
						<button type="submit" name="do_it_now" class="w3-btn">Submit</button>
					</form>		
				</div>
				<div id="db2" class="w3-panel example" style="display:none">
					<h3>Visitor comments</h3>
					<?php
					$comment = getData($qry_Comments);
					if (!$comment) {
						echo 'No comments to display';
					}
					else {
						echo '<table style="width:85%">';
						echo '<tr><th>Comment</th><th style="padding-left: 10px;width: 100px">Date</th></tr>';
						foreach ($comment as $row) {
							echo '<tr><td>'.$row['comment'].'</td><td>'.$row['entry_dt'].'</td></tr>';
						}
						echo '</table>';
					}					
					?>
					</table>
				</div>
				<div id="db3" class="w3-panel example" style="display:none">
					<h3>Books by genre</h3>
					<!-- <p>Column headings can be used to sort the entries</p> -->
					<?php
					$bookList = getData($qry_GenBkAuth);
					if (!$bookList) {
						echo '<p>No genre relationships to display</p>';
					}
					else {
						echo '<table style="width:85%">';
						echo '<tr><th class="left-algn">Genre</th><th class="left-algn">Book title</th><th class="left-algn">Author</th></tr>';

						foreach ($bookList as $row) {
							echo '<tr><td>'.$row['genre'].'</td><td>'.$row['title'].'</td><td>'.$row['author'].'</td></tr>';					
						}
						echo '</table>';
					}
					?>
				</div>
				<div id="db4" class="w3-panel example" style="display:none">
					<h3>Books by language</h3>
					<?php
					$bookList = getData($qry_LangBkAuth);
					if (!$bookList) {
						echo '<p>No language relationships to display</p>';
					}
					else {
						echo '<table style="width:85%">';
						echo '<tr><th class="left-algn">Language</th><th class="left-algn">Book title</th><th class="left-algn">Author</th></tr>';
						foreach ($bookList as $row) {
							echo '<tr><td>'.$row['language'].'</td><td>'.$row['title'].'</td><td>'.$row['author'].'</td></tr>';
						}
						echo '</table>';						}
					?>
				</div>
			</div>
		</div>
	</body>
	<footer id="pg_footer">
		<div class="w3-col s12 m12 l12 w3-right-align w3-margin-bottom">
			<p class="w3-margin-right">Last updated: 02-05-2018</p>
		</div>
	</footer>
	<?php

	// As suggested by W3.Schools tutorial
	if ($_SERVER["REQUEST_METHOD"] == "POST") {
		$email = test_input($_POST["your_email"]);
		$text = test_input($_POST["your_text"]);
		addCommment($email, $text);
	}

	// As suggested by W3.Schools tutorial
	function test_input($data) {
		$data = trim($data);
		$data = stripslashes($data);
		$data = htmlspecialchars($data);
		return $data;
	}	
	
	// Function to connect to the database and return connection handle
	function dbopen() {
		return pg_connect("host=localhost port=5432 dbname=mywebstuff user=username password=password connect_timeout=5");
	}

	// Function to retrieve records	
	function getData($dbqry) {
		$dbconn = dbopen();
		$rs = pg_query($dbconn, $dbqry);
		if (!$rs) {
			return false;
		}
		else {
			return pg_fetch_all($rs);
		}
	}
	
	// Function to insert a record
	function addCommment($fld1, $fld2) {
		$dbconn = dbopen();
		$dbqry = "Insert into examples.comments(email, comment)"
				. "VALUES ('".$fld1."','".$fld2."')";
		pg_query($dbconn, $dbqry);
	}
	?>
</html>