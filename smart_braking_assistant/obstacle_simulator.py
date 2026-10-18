import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class ObstacleSimulator(Node):
    def __init__(self):
        super().__init__('obstacle_simulator')
        self.publisher_ = self.create_publisher(Float32, 'front_distance', 10)
        self.timer = self.create_timer(1.0, self.timer_callback) # állítható milyen gyorsan változzon
        self.current_distance = 15.0 #alaptávolság érték, úgyszintén állítható

    def timer_callback(self):
        msg = Float32()
        msg.data = self.current_distance
        self.publisher_.publish(msg)
        self.get_logger().info(f'[Szimulátor] Távolság az akadálytól: {self.current_distance:.1f} m')

        #Közelebb megyünk minden másodpercben
        self.current_distance -= 1.5

        if self.current_distance < 0.0:
            self.current_distance = 15.0
            self.get_logger().info(f'[Szimulátor] Újraindítás, 15 méterről')

def main(args=None):
    rclpy.init(args=args)
    node = ObstacleSimulator()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()