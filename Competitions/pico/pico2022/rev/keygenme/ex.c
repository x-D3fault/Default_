#include <stdio.h>
#include <string.h>
#include <openssl/md5.h>

int main() {
	char * pico = "picoCTF{";
	size_t pico_length = strlen(pico);
	char pico_bytes[16];
	MD5(pico, pico_length, pico_bytes);
	char readable_pico_bytes[14] ;
	int n = 0;
	for (int i = 0; i < 16; i++) {
		sprintf(readable_pico_bytes + n, "%02x", pico_bytes[i]);
		printf("%02x", pico_bytes[i]);
		n = n + 2;
	}

	char * curl = "}";
	size_t curl_length = strlen(curl);
	char curl_bytes[16];
	MD5(curly, curl_length, curl_bytes);

	int n = 0;	
	char readable_curly[21];
	for (int i = 0; i < 16; i++) {
		sprintf(readable_curly + n, "%02x", curl_bytes[i]);
	}
	return 0;
}
