from util.queue import Queue
from util.packet import Packet
from util.config import LARGE_NUMBER
from util.util import exponential_random


class ThreeQueueSimulator:
    def __init__(self, end_time, lambda_value, mu, packet_size):
        self.end_time = end_time
        self.lambda_value = lambda_value
        self.mu = mu
        self.packet_size = packet_size

    def run(self):
        self.next_arrival_time_1 = exponential_random(1/self.lambda_value)
        self.next_departure_time_1 = LARGE_NUMBER
        self.next_arrival_time_2 = LARGE_NUMBER
        self.next_departure_time_2 = LARGE_NUMBER
        
        self.next_arrival_time_3 = LARGE_NUMBER
        self.next_departure_time_3 = LARGE_NUMBER
        
        self.buffer_1 = Queue()
        self.buffer_2 = Queue()
        self.buffer_3 = Queue()

        self.packets_served_number = 0
        self.all_packet_delays_sum = 0
        self.packets_arrived_number = 0

        time = 0
        while time <= self.end_time:
            time = min(self.next_arrival_time_1, self.next_departure_time_1, self.next_arrival_time_2, self.next_departure_time_2, self.next_arrival_time_3, self.next_departure_time_3)

            # first queue
            if self.next_arrival_time_1 == time:
                self.buffer_1.insert(Packet(time, self.packet_size))
                self.packets_arrived_number += 1
                self.next_arrival_time_1 = time + exponential_random(1/self.lambda_value)

                if self.next_departure_time_1 == LARGE_NUMBER:
                    self.next_departure_time_1 = time + exponential_random(1/self.mu)

            if self.next_departure_time_1 == time:
                self.last_packet_serverd_in_buffer_1 = self.buffer_1.delete()

                if self.buffer_1.is_empty():
                    self.next_departure_time_1 = LARGE_NUMBER
                
                else:
                    self.next_departure_time_1 = time + exponential_random(1/self.mu)

                self.next_arrival_time_2 = time 

            # second queue
            if self.next_arrival_time_2 == time:
                self.buffer_2.insert(self.last_packet_serverd_in_buffer_1)
                self.next_arrival_time_2 = LARGE_NUMBER
                
                if self.next_departure_time_2 == LARGE_NUMBER:
                    self.next_departure_time_2 = time + exponential_random(1/self.mu)

            if self.next_departure_time_2 == time:
                self.last_packet_serverd_in_buffer_2 = self.buffer_2.delete()

                if self.buffer_2.is_empty():
                    self.next_departure_time_2 = LARGE_NUMBER

                else:
                    self.next_departure_time_2 = time + exponential_random(1/self.mu)

                self.next_arrival_time_3 = time 

            # third queue
            if self.next_arrival_time_3 == time:
                self.buffer_3.insert(self.last_packet_serverd_in_buffer_2)
                self.next_arrival_time_3 = LARGE_NUMBER
                
                if self.next_departure_time_3 == LARGE_NUMBER:
                    self.next_departure_time_3 = time + exponential_random(1/self.mu)

            if self.next_departure_time_3 == time:
                self.last_packet_serverd_in_buffer_3 = self.buffer_3.delete()
                
                packet_delay = time - self.last_packet_serverd_in_buffer_3.arrival_time
                self.all_packet_delays_sum += packet_delay
                self.packets_served_number += 1

                if self.buffer_3.is_empty():
                    self.next_departure_time_3 = LARGE_NUMBER

                else:
                    self.next_departure_time_3 = time + exponential_random(1/self.mu)

        self.simulated_average_packet_delay = self.all_packet_delays_sum / self.packets_served_number
        self.simulated_packet_arrival_probability = self.packets_arrived_number / self.end_time
        self.analytical_avgerage_packet_delay = 3 * (1/(self.mu - self.lambda_value))


class TwoQueueSimulator:
    def __init__(self, end_time, lambda_value, mu, packet_size):
        self.end_time = end_time
        self.lambda_value = lambda_value
        self.mu = mu
        self.packet_size = packet_size

    def run(self):
        self.next_arrival_time_1 = exponential_random(1/self.lambda_value)
        self.next_departure_time_1 = LARGE_NUMBER
        self.next_arrival_time_2 = LARGE_NUMBER
        self.next_departure_time_2 = LARGE_NUMBER
        
        self.buffer_1 = Queue()
        self.buffer_2 = Queue()

        self.packets_served_number = 0
        self.all_packet_delays_sum = 0
        self.packets_arrived_number = 0

        time = 0
        while time <= self.end_time:
            time = min(self.next_arrival_time_1, self.next_departure_time_1, self.next_arrival_time_2, self.next_departure_time_2)

            # first queue
            if self.next_arrival_time_1 == time:
                self.buffer_1.insert(Packet(time, self.packet_size))
                self.packets_arrived_number += 1
                self.next_arrival_time_1 = time + exponential_random(1/self.lambda_value)

                if self.next_departure_time_1 == LARGE_NUMBER:
                    self.next_departure_time_1 = time + exponential_random(1/self.mu)

            if self.next_departure_time_1 == time:
                self.last_packet_serverd_in_buffer_1 = self.buffer_1.delete()

                if self.buffer_1.is_empty():
                    self.next_departure_time_1 = LARGE_NUMBER
                
                else:
                    self.next_departure_time_1 = time + exponential_random(1/self.mu)

                self.next_arrival_time_2 = time 

            # second queue
            if self.next_arrival_time_2 == time:
                self.buffer_2.insert(self.last_packet_serverd_in_buffer_1)
                self.next_arrival_time_2 = LARGE_NUMBER
                
                if self.next_departure_time_2 == LARGE_NUMBER:
                    self.next_departure_time_2 = time + exponential_random(1/self.mu)

            if self.next_departure_time_2 == time:
                packet = self.buffer_2.delete()
                
                packet_delay = time - packet.arrival_time
                self.all_packet_delays_sum += packet_delay
                self.packets_served_number += 1

                if self.buffer_2.is_empty():
                    self.next_departure_time_2 = LARGE_NUMBER

                else:
                    self.next_departure_time_2 = time + exponential_random(1/self.mu)

        self.simulated_average_packet_delay = self.all_packet_delays_sum / self.packets_served_number
        self.simulated_packet_arrival_probability = self.packets_arrived_number / self.end_time
        self.analytical_avgerage_packet_delay = 2 * (1/(self.mu - self.lambda_value))
