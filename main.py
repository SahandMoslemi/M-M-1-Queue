from simulation.simulator import TwoQueueSimulator, ThreeQueueSimulator
from plotting.plotter import TwoFunctionPlotter


if __name__ == '__main__':
    lambda_values_1 = [5 + 0.5 * i for i in range(8)]
    simulated_average_packet_delay_values_1 = []
    analytical_avgerage_packet_delay_values_1 = []

    for lambda_value in lambda_values_1:
        # simulation = TwoQueueSimulator(end_time=5000, lambda_value=lambda_value, mu=10, packet_size=1)
        simulation = ThreeQueueSimulator(end_time=10000, lambda_value=lambda_value, mu=10, packet_size=1)
        simulation.run()

        simulated_average_packet_delay_values_1.append(simulation.simulated_average_packet_delay)
        analytical_avgerage_packet_delay_values_1.append(simulation.analytical_avgerage_packet_delay)

    plotter_1 = TwoFunctionPlotter(
        lambda_values_1, 
        simulated_average_packet_delay_values_1,
        'Simulation',
        analytical_avgerage_packet_delay_values_1, 
        'Analysis',
        'Lambda Value', 'Delay'
        )
    plotter_1.plot()