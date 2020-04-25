# crocodile 鳄鱼
import math
import sys
import matplotlib.pyplot as plt


class CrocodileIsland():
    PI = math.pi
    # 岛的半径
    R = 100
    # 鳄鱼初始位置, 极坐标
    croco_position = math.pi/2
    # 小明初始位置, 直角坐标
    person_position = (0, 0)
    # 鳄鱼的速度
    croco_speed = 4
    # 小明的速度
    person_speed = croco_speed/4

    is_win = False

    # 获取鳄鱼到岛边某位置的距离
    def get_croco_distantce(self, theta):
        '''
        theta: 岛上某位置的极坐标的角度
        '''
        t = abs(theta-self.croco_position)
        t = t if t < math.pi else 2*math.pi-t
        return self.R*t

    # 获取小明到岛边某位置的距离
    def get_person_distantce(self, theta):
        '''
        theta: 岛上某位置的极坐标的角度
        '''
        island_position = (self.R*math.cos(theta), self.R*math.sin(theta))
        return math.sqrt((self.person_position[0]-island_position[0])**2 + (self.person_position[1]-island_position[1])**2)

    # 遍历圆, 得到人逃离的最佳方向
    def get_best_theta(self):
        best_theta = 0
        best_rate = 0
        split_count = 360
        for i in range(split_count):
            theta = 2*math.pi/split_count*i
            croco_distance = self.get_croco_distantce(theta)
            person_distance = self.get_person_distantce(theta)
            rate = croco_distance/person_distance #注意要相除, 不能相减
            if rate > best_rate:
                best_rate = rate
                best_theta = theta
        print("best_theta", best_theta, best_theta/math.pi*180, self.get_croco_distantce(best_theta)/self.get_person_distantce(best_theta))
        return best_theta

    # 获得鳄鱼移动方向;顺时针返回-1, 逆时针返回1;
    def get_croco_move_direction(self):
        # 人的位置转为极坐标的方向
        (x, y) = self.person_position
        theta = math.atan2(y, x)
        theta = theta if theta > 0 else 2*math.pi + theta
        diff = theta - self.croco_position
        if diff > math.pi:
            return -1
        elif diff > 0:
            return 1
        elif diff < -1*math.pi:
            return 1
        elif diff == 0: 
            return 0
        else:
            return -1

    # 移动人和鳄鱼
    def move(self):
        theta = self.get_best_theta()
        # 假定每一秒钟移动一次
        time = 1
        # 计算鳄鱼的位置
        # 移动的角度
        theta_diff = time*self.croco_speed/self.R
        self.croco_position = self.croco_position + self.get_croco_move_direction()*theta_diff
        self.croco_position = self.croco_position % (
            2*math.pi)  # 确保croco_position范围是[0,2*pi)

        # 计算人的位置, 向量平移
        island_position = (self.R*math.cos(theta), self.R*math.sin(theta))
        position_vector = (
            island_position[0]-self.person_position[0], island_position[1]-self.person_position[1],)
        distance = math.sqrt(position_vector[0]**2+position_vector[1]**2)
        position_vector = (position_vector[0]/distance, position_vector[1]/distance)  # 转为单位向量
        self.person_position = (self.person_position[0]+self.person_speed*time*position_vector[0],
                                self.person_position[1]+self.person_speed*time*position_vector[1])

        # 判断已经成功逃离
        x,y = self.person_position
        if x**2+y**2 >= self.R**2:
            self.is_win = True

    # 得到鳄鱼位置的直角坐标;
    def get_croco_position(self):
        return (self.R * math.cos(self.croco_position), self.R*math.sin(self.croco_position))

    # 绘图
    def press(self, event):
        fig = self.fig
        ax = self.ax
        sys.stdout.flush()
        if event.key == ' ':
            if self.is_win:
                self.ax.set_title('eyudao - you win')
                fig.canvas.draw()
                return

            self.move()
            croco = self.get_croco_position()
            person = self.person_position
            if self.croco_point:
                self.croco_point[0].remove()
            self.croco_point = ax.plot(croco[0], croco[1], 'r^')
            ax.plot(croco[0], croco[1], 'yo', markersize = 2.0)

            if self.person_point:
                self.person_point[0].remove()
            self.person_point = ax.plot(person[0], person[1], 'ro', markersize = 8.0)
            ax.plot(person[0], person[1], 'yo', markersize = 2.0)

            fig.canvas.draw()

    def plot(self):
        fig, ax = plt.subplots()
        self.fig = fig
        self.ax = ax
        self.croco_point = []
        self.person_point = []

        fig.canvas.mpl_connect('key_press_event', self.press)

        circle = plt.Circle((0, 0), self.R, color='g')
        ax.add_artist(circle)

        axis_width = self.R+5
        ax.axis([-1*axis_width, axis_width, -1 * axis_width, axis_width])
        ax.set_aspect('equal', adjustable='box', anchor='C')
        ax.set_title('eyudao')
        plt.show()

    def main(self):
        self.plot()


if __name__ == "__main__":
    a = CrocodileIsland()
    a.main()
