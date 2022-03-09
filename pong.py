import rospy
from std_msgs.msg import Int64



def check_ping(msg):
	
	if msg.data == 'ping':
	    
	    new_msg.data = 'pong'
    else:
        new_msg.data = 'casi'

	pub.publish(new_msg)
	rospy.loginfo( msg.data)

rospy.init_node('check_ping')
pub = rospy.Publisher("entrada",String, queue_size=10)
sub = rospy.Subscriber("entrada", String, check_ping)
rospy.spin()