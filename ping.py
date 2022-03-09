import rospy
import random
from std_msgs.msg import Int64

rospy.init_node("number_publisher", anonymous=True)
pub = rospy.Publisher("/number", std_msgs.msg.String, queue_size=10)
rate = rospy.Rate(1)

while not rospy.is_shutdown():
	msg = random.randint(0,1)
    if a % 2 == 0:
	    msg.data = 'ping'
    else:
        msg.data = 'not ping'

	pub.publish(msg)
	rate.sleep()
    