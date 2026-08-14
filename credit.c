#include <cs50.h>
#include <math.h>
#include <stdio.h>

int len(long number);
int typecard(long number, int digit_position);

int main(void)
{
    // getting the last digit to first for the checksum that wasn't doubled
    long card = get_long("Card's number: ");
    int sum1 = 0;
    int sum2 = 0;
    long result = card;
    int verifier;
    int final_verifier;
    int length = len(card);
    for (double div = 1; result > 1; div *= 100)
    {
        result = (card / div);
        verifier = result % 10;
        sum1 += verifier;
    }
    // redefining the last variables for the second sum
    result = card;
    verifier = 0;
    // second sum
    int double_verifier;
    int separe_digits;
    for (double div = 10; result > 1; div *= 100)
    {
        result = (card / div);
        verifier = result % 10;
        double_verifier = verifier * 2;
        if (double_verifier >= 10)
        {
            separe_digits = (double_verifier % 10) + 1;
            sum2 += separe_digits;
        }
        else
        {
            sum2 += double_verifier;
        }

    }
    // verifying the digit
    final_verifier = (sum2 + sum1) % 10;

    if (final_verifier == 0)
    {
        // searching the type of card
        int mastercard = typecard(card, 2);
        int american = typecard(card, 2);
        int visa = typecard(card, 1);
        if (visa == 4 && (length == 13 || length == 16))
        {
            printf("VISA\n");
        }
        else if ((american == 34 || american == 37) && (length == 15))
        {
            printf("AMEX\n");
        }
        else if ((mastercard == 51 || mastercard == 52 || mastercard == 53 || mastercard == 54 ||
                  mastercard == 55) &&
                 (length == 16))
        {
            printf("MASTERCARD\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}

int len(long number)
{
    long div = 10;
    int digit_numbers = 0;
    long result = number;
    while (result >= 1)
    {
        digit_numbers += 1;
        result = number / div;
        div *= 10;
    }
    return digit_numbers;
}
int typecard(long number, int digit_index)
{
    int length = len(number);
    long find_digits = pow(10, length - digit_index);
    long initial_digits = number / find_digits;
    return initial_digits;
}
