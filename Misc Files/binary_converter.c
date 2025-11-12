#include <stdio.h>
#include <stdbool.h>

int getInt();

int main() {
	printf("Please input integer (0, 255): ");
	
	short value = getInt();
	bool wholeNumber[8];

	printf("\n");

	//only works for standard notation
	for (int i = 7; i >= 0; i--) {
		//writes true if odd, false if even
		wholeNumber[i] = value % 2;

		value /= 2;
	}

	for (int i = 0; i < 8; i++) {
		printf("%s", wholeNumber[i] ? "1" : "0");
	}

	printf("\n");

	return 0;
}

//gets an integer from the user
int getInt() {
	int number;
	scanf("%d", &number);
	return number;
}
