# region imports
import math
#endregion

def Probability(PDF, args=(), GT=True):
    """
  Determine the probability by applying Simpson's 1/3 rule to a specified Gaussian/normal probability density function.

    Parameters:
    PDF (callable): A callback function for the Gaussian/normal probability density function.
    args (tuple): A tuple that includes x, μ, and σ.
    GT (bool): True if the probability of x being greater than x_0, False otherwise.

    Returns:
    float: The calculated probability value.
    """
    x, mu, sigma = args
    lower_limit = -5 * sigma
    upper_limit = x

    # Number of intervals for Simpson's 1/3 rule
    num_intervals = 1000
    interval_width = (upper_limit - lower_limit) / num_intervals

    # Calculate probability using Simpson's 1/3 rule
    probability = 0
    for i in range(num_intervals + 1):
        xi = lower_limit + i * interval_width
        yi = PDF((xi, mu, sigma))

        # Apply Simpson's 1/3 rule formula
        if i == 0 or i == num_intervals:
            probability += yi
        elif i % 2 == 1:
            probability += 4 * yi
        else:
            probability += 2 * yi

    probability *= interval_width / 3

    # Adjust probability based on whether we want P(x > x_0) or P(x < x_0)
    if GT:
        probability = 1 - probability

    return probability


def gaussian_pdf(args):
    """
    Gaussian/normal probability density function.


    """
    x, mu, sigma = args
    exponent = -((x - mu) ** 2) / (2 * sigma ** 2)
    return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(exponent)


def main():
    """
    Main function to calculate and print probabilities.
    """
    # prob 1
    x1 = 105.00
    mu1, sigma1 = 100, 12.5
    prob1 = Probability(gaussian_pdf, (x1, mu1, sigma1), GT=False)
    print(f'P(x<{x1:.2f}|μ={mu1},{sigma1})={prob1:.3f}')

    # prob 2
    x2 = 120.00
    mu2, sigma2 = 100, 15
    prob2 = Probability(gaussian_pdf, (x2, mu2, sigma2), GT=True)
    print(f'P(x>{x2:.2f}|μ={mu2},{sigma2})={prob2:.3f}')


if __name__ == "__main__":
    main()