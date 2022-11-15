import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def estimate_coef(predictor, response):
    observations_count = np.size(predictor)

    predictor_mean = np.mean(predictor)
    response_mean = np.mean(response)

    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(response * predictor) - observations_count * response_mean * predictor_mean
    SS_xx = np.sum(predictor * predictor) - observations_count * predictor_mean * predictor_mean

    # calculating regression coefficients
    slope = SS_xy / SS_xx
    intercept = response_mean - slope * predictor_mean

    return intercept, slope


def plot_regression_line(predictor, response, coeff_estimates):
    # plotting the actual points as scatter plot
    plt.scatter(predictor, response, color="m",
                marker="o", s=30)

    # predicted response vector
    y_pred = coeff_estimates[0] + coeff_estimates[1] * predictor

    # plotting the regression line
    plt.plot(predictor, y_pred, color="g")

    plt.xlabel("Year")
    plt.ylabel('Headline Consumer Inflation Rate Annually')
    plt.legend(["USA HCPI"])
    plt.title('Headline Consumer Price Inflation, United States')
    plt.show()


def model_annual_headline_consumer_price_index(predictor, response):
    coeff_estimates = estimate_coef(predictor, response)

    # plotting regression line
    plot_regression_line(predictor, response, coeff_estimates)
