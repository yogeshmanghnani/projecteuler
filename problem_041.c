#include<stdio.h>
#include<stdbool.h>
#include<stdlib.h>

bool is_pandigital(long number){
	long n = number;
	int totalDigits = 0;
	int digit;
	while(n!=0){
		n=n/10;
		totalDigits++;
	}
	n = number;
	bool arr[totalDigits];
	for(int a=0; a<totalDigits; a++){
		arr[a] = false;
	}
	while(n!=0){
		digit = n%10;
		n=n/10;
		if(digit<=totalDigits && digit>=1){
			arr[digit-1] = true;
		}
	}

	for(int a=0; a<totalDigits; a++){
		if(!arr[a]){
			return false;
		}
	}
	return true;
}


long mark_pandigitals(bool *arr, long total){
	long last = 0;
	for(int i=0; i<total; i++){
		if(arr[i]){
			if(is_pandigital(i)){
				last = i;
			}else{
				arr[i] = false;
			}
		}
	}

	return last;
}




int main(){
	long i = 0;
	long total = 1000000000;
	bool *arr = malloc(total * sizeof(bool));
	for(i = 0; i<total; i++){
		arr[i] = true;
	}
	arr[0] = false;
	arr[1] = false;
	

	//Starting to mark composite false
	for(i=2; i<total; i++){
		if(!arr[i]){
			continue;
		}
		long up = (total/i)+1;
		for(long m=2; m<up; m++){
			arr[i*m] = false;
		}
	}
	printf("%ld", mark_pandigitals(arr, total));
	return 0;
}
