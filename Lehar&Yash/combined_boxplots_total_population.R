#Installing necessary packages
installed.packages("ggplot2")
install.packages("scales")
installed.packages("gridExtra")
installed.packages("crayon")

#loading necessary packages
library(ggplot2)
library(scales)
library(gridExtra)
library(crayon)

# Read the CSV files
data_1991 <- read.csv("C://Users//user//OneDrive//Desktop//CENSUSyear1991.csv")
data_2001 <- read.csv("C://Users//user//OneDrive//Desktop//2001 Data Education^J Population^J Religion^J Workers.csv")
data_2011 <- read.csv("C://Users//user//OneDrive//Desktop//2011 Data Education^J Population^J Religion^J Workers.csv")

# Creating Function to generate the plot for a given year and data
generate_plot <- function(data, year, y_limits) {
  # For Calculating summary statistics and handling missing values
  mean_pop <- mean(data$Total_Population, na.rm = TRUE)
  quartiles <- quantile(data$Total_Population, probs = c(0.25, 0.5, 0.75), na.rm = TRUE)
  
  # Create the box plot
  p <- ggplot(data, aes(x = "", y = Total_Population)) +
    geom_boxplot(fill = "grey", color = "blue", notch = FALSE, outlier.color = "red", outlier.shape = 8) +
    geom_hline(aes(yintercept = mean_pop), linetype = "dotted", color = "red") +
    labs(title = paste("Total Population -", year), y = "") +
    coord_cartesian(ylim = y_limits) + # y-axis limits for zooming
    scale_y_continuous(labels = scales::comma) +  # Formating y-axis labels to normal numbers
    theme_minimal() +
    theme(plot.title = element_text(hjust = 0.5)) +  # For Centering the plot title
    annotate("text", x = 1.2, y = mean_pop, label = paste("Mean:", round(mean_pop, 2)), color = "black", size = 4.0, hjust = 0) +
    annotate("text", x = 1.2, y = quartiles[1], label = paste("Q1:", round(quartiles[1], 2)), color = "darkgreen", size = 4.0, hjust = 0) +
    annotate("text", x = 1.2, y = quartiles[2], label = paste("Median:", round(quartiles[2], 2)), color = "black", size = 4.0, hjust = 0) +
    annotate("text", x = 1.2, y = quartiles[3], label = paste("Q3:", round(quartiles[3], 2)), color = "darkgreen", size = 4.0, hjust = 0)
  
  return(p)
}

# Determine common y-axis limits
y_limits <- c(0, 200000000)

# Generate plots for each year with the same y-axis limits
plot_1991 <- generate_plot(data_1991, "1991", y_limits)
print("Plot for 1991 generated.")

plot_2001 <- generate_plot(data_2001, "2001", y_limits)
print("Plot for 2001 generated.")

plot_2011 <- generate_plot(data_2011, "2011", y_limits)
print("Plot for 2011 generated.")

# Save each plot individually to the Desktop
ggsave("C://Users//user//OneDrive//Desktop//boxplot_total_population_1991.png", plot = plot_1991)
print("Plot for 1991 saved.")

ggsave("C://Users//user//OneDrive//Desktop//boxplot_total_population_2001.png", plot = plot_2001)
print("Plot for 2001 saved.")

ggsave("C://Users//user//OneDrive//Desktop//boxplot_total_population_2011.png", plot = plot_2011)
print("Plot for 2011 saved.")

# Display the individual plots
print(plot_1991)
print(plot_2001)
print(plot_2011)

# Combine the plots into one figure in a single row
combined_plot <- grid.arrange(plot_1991, plot_2001, plot_2011, nrow = 1)
print("Combined plot created.")

# Save the combined plot to the Desktop
ggsave("C://Users//user//OneDrive//Desktop//combined_boxplots_total_population.png", plot = combined_plot, height = 6, width = 18)
print("Combined plot saved.")

# Console output using crayon for better readability
cat(yellow("Plots for each census year have been generated and saved.\n"))
cat(green("Combined plot has been saved as 'combined_boxplots_total_population.png'.\n"))