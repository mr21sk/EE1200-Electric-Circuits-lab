import numpy as np
import matplotlib.pyplot as plt

def lissajous_figure(A, B, a, b, delta, t_max=2*np.pi, num_points=100000):
    """
    Generate and plot a Lissajous figure.

    Parameters:
        A (float): Amplitude of the sine wave along the x-axis.
        B (float): Amplitude of the sine wave along the y-axis.
        a (float): Ratio of frequencies along the x-axis.
        b (float): Ratio of frequencies along the y-axis.
        delta (float): Phase difference between the two waves (in radians).
        t_max (float): The maximum value of t to plot (default is 2*pi).
        num_points (int): Number of points to plot (default is 1000).
    """
    # Generate time points
    t = np.linspace(0, t_max, num_points)

    # Compute x and y
    x = A * np.sin(a * t + delta)
    y = B * np.sin(b * t)

    # Plot the figure
    plt.figure(figsize=(8, 8))
    plt.plot(x, y, label=f"a={a}, b={b}, delta={np.degrees(delta):.2f} degrees")
    plt.title("Lissajous Figure")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.axis("equal")
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage
if __name__ == "__main__":
    # Ask user for parameters
    print("Phase difference (delta) should be entered in degrees.")
    A = float(input("Enter amplitude along x-axis (A): "))
    B = float(input("Enter amplitude along y-axis (B): "))
    a = float(input("Enter frequency ratio along x-axis (a): "))
    b = float(input("Enter frequency ratio along y-axis (b): "))
    delta_degrees = float(input("Enter phase difference in degrees (delta): "))
    delta = np.radians(delta_degrees)  # Convert degrees to radians

    lissajous_figure(A, B, a, b, delta)

