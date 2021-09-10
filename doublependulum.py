from numpy import sin, cos , pi
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import matplotlib.animation as animation
try:
    
    doyou = input("""We have two already mad stimulation press (s) to see the stimulation for small angle 
and (l) for longer angle , press (c) to continue with our initial values :""")
    if doyou.strip().upper() == 'L'  :
        M1 = 1
        M2 = 1
        L1 =  1
        L2 =  1
        g = 9.81
        AD1 = 3*pi/7
        AD2 = 3*pi/4
        AV1 = 0
        AV2 = 0
        maxtime = 30
        
    if doyou.strip().upper() == 'S'  :
        M1 = 1
        M2 = 1
        L1 =  1
        L2 =  1
        g = 9.81
        AD1 = pi/4
        AD2 = pi/6
        AV1 = 0
        AV2 = 0
        maxtime = 30
    
    if doyou.strip().upper() == 'C'  :
        M1 = eval(input("Enter the mass of the first bob : "))
        M2 = eval(input("Enter the mass of the second bob : "))
        L1 =  eval(input("Enter the lenght of the first rod : "))
        L2 =  eval(input("Enter the lenght of the second rod : "))
        g = eval(input("Enter the value of gravitational accelaration : "))
        AD1 = eval(input("Enter the initial angular displacement of first bob : "))
        AD2 = eval(input("Enter the initial angular displacement of second bob : "))
        AV1 = eval(input("Enter the initial angular velocity of first bob : "))
        AV2 = eval(input("Enter the initial angular velocity of second bob : "))
        maxtime = eval(input("Enter the maximum time limit for stimulation : "))
    
    
    def system_equation(initial_value , t):
        omega_1 = initial_value[1]
        omega_2 = initial_value[3]
        th1 ,th2 = initial_value[0] , initial_value[2]
        delta_theta = th1 - th2 
        sth1 = sin(th1) 
        sth2 = sin(th2) 
        s , c = sin(delta_theta) , cos(delta_theta)
        denominator_constant = M1 + M2 * (s*s)
        
        omega_1dot = ( M2*g*sth2*c-M2*s*(L1*omega_1*omega_1*c+L2*omega_2*omega_2)-(M1+M2)*g*sth1)/(L1*denominator_constant)
        omega_2dot = ((M1+M2)*(L1*omega_1*omega_1*s-g*sth2+g*sth1*c)+M2*L2*omega_2*omega_2*s*c)/(L2*denominator_constant)
        
        return omega_1 , omega_1dot , omega_2 , omega_2dot
    
    
    dt = 0.005
    t = np.arange(0.0, maxtime, dt)
    
    
    
    initial_value = [AD1 , AV1 , AD2 , AV2 ]
    
    theta_values = odeint(system_equation , initial_value , t)
    
    x1 = L1*sin(theta_values[:, 0])
    y1 = -L1*cos(theta_values[:, 0])
    
    x2 = L2*sin(theta_values[:, 2]) + x1
    y2 = -L2*cos(theta_values[:, 2]) + y1
    #------------------------------------------------------------------------------------
    
    
    
    
    
    fig = plt.figure(figsize=(4,4))
    ax1  = fig.add_subplot(111, autoscale_on=True,  xlim=(-1*(L1+L2) , (L1+L2)),ylim = (-1*(L1+L2) , (L1+L2)))
    ax1.grid()
    ax1.title.set_text('Double Pendulum')
    
    line, = ax1.plot([], [], 'o-', lw=2)
    line1, = ax1.plot([],[] , '-r' )
    line2, = ax1.plot([],[] , '-g' )
    time_template = 'time = %.1fs'
    time_text = ax1.text(0.05, 0.9, '', transform=ax1.transAxes)
    
    
    def init():
        line.set_data([], [])
        line1.set_data([], [])
        line2.set_data([], [])
        time_text.set_text('')
        return line, time_text ,line1 , line2
    
    
    x1data , y1data = [] , []
    x2data , y2data = [] , []
    def animate(i):
        thisx = [0, x1[i], x2[i]]
        thisy = [0, y1[i], y2[i]]
        x1data.append(x1[i])
        y1data.append(y1[i])
        x2data.append(x2[i])
        y2data.append(y2[i])
    
        if i > 300 :
            x1data.pop(0)
            y1data.pop(0)
            x2data.pop(0)
            y2data.pop(0)
            
        if i == len(theta_values)-1:
            x1data.clear()
            x2data.clear()
            y1data.clear()
            y2data.clear()
            
        line1.set_data(x2data , y2data)
        line2.set_data(x1data , y1data)
        line.set_data(thisx, thisy)
        time_text.set_text(time_template % (i*dt))
        
        
        return line, time_text , line1 , line2
    
    fig.canvas.manager.window.move(0,0)
    ani1 = animation.FuncAnimation(fig, animate,np.arange(1, len(theta_values)),
                                  interval=1, blit=True, init_func=init )
    #--------------------------------------------------------------------------------------
    
    
    
    
    
    
    fig1 = plt.figure(figsize=(4,4))
    ax2 = fig1.add_subplot(111, autoscale_on=True, 
                           xlim=(-1*(L1+L2) , (L1+L2)),ylim = (-1*(L1+L2) , (L1+L2)))
    ax2.grid()
    ax2.title.set_text('x1 VS x2')
    
    line3, = ax2.plot([],[] ,lw =1)
    
    def init1():
        line3.set_data([],[])
        return line3,
    
    x_1data,x_2data = [],[]
    def animate1(i):
        x_1data.append(x1[i])
        x_2data.append(x2[i])
        line3.set_data(x_1data,x_2data)
        
        if i == len(theta_values)-1:
            x_1data.clear()
            x_2data.clear()
        
       
        return line3,
    
    fig1.canvas.manager.window.move(975,0)
    ani2 = animation.FuncAnimation(fig1, animate1, np.arange(1, len(theta_values)),
                                    interval=1, blit=True, init_func=init1 )  
    #---------------------------------------------------------------------------------------
    
    
    
    def makeplot(x1,x2 , y_limit,position ,name = None):
    
        fig2 = plt.figure(figsize=(6.5,2))
        ax3 = fig2.add_subplot(111, autoscale_on=True, 
                               ylim = y_limit , xlim = (min(t),max(t)))
        
        ax3.grid()
        ax3.title.set_text(f'''{name} vs Time''')
        
        line4 , = ax3.plot([],[] ,'-r',lw = 1 , alpha = 0.95)
        line5 , = ax3.plot([],[] ,'-g',lw = 1, alpha = 0.95)
        line6 , = ax3.plot([],[] ,'-k',lw = 1.15)
        line7 , = ax3.plot([],[] ,'-b',lw = 2)
        
        def init2():
            line4.set_data([] ,[])
            line5.set_data([],[])
            line6.set_data([],[])
            line7.set_data([],[])
            return line4 , line5,line6,line7,
        
        x1t , x2t ,xsum , time , = [] , [] , [] , []
        def animate2(i):
            x1t.append(x1[i])
            x2t.append(x2[i])
            xsum.append(x1[i]+x2[i])
            time.append(t[i])
            xvalue = [x1[i]+x2[i] , x2[i] ,x1[i]]
            yvalue = [t[i],t[i],t[i]]
            
            
            line4.set_data(time , x2t)
            line5.set_data(time , x1t)
            line6.set_data(time , xsum)
            line7.set_data(yvalue , xvalue)
            
            
            if i == len(theta_values)-1:
                x1t.clear()
                x2t.clear()
                xsum.clear()
                time.clear()
          
            
            return line4 , line5 , line6, line7,
        
        
        fig2.canvas.manager.window.move(position[0],position[1])
        
        ani3 = animation.FuncAnimation(fig2, animate2, np.arange(1, len(theta_values))
                                         ,interval=1, blit=True, init_func=init2)
        return ani3
    
    
    
    
    
    outer_ani1 = makeplot(x1,x2 , (-1*(max(x1)+max(x2)+1) , (max(x1)+max(x2)+1))  
                                     ,(0,450),'x')
    outer_ani2 = makeplot(y1,y2 , (-3 , 1)  ,(725,450) , 'y')
    
    
    fig3 = plt.figure(figsize = (5,4))
    
    ax4 = fig3.add_subplot(111, autoscale_on=True,  xlim=(-1*(L1+L2) , (L1+L2)),ylim = (-1*(L1+L2) , (L1+L2)))
    
    ax4.grid()
    
    line8, = ax4.plot([],[] ,'-r',lw = 2)
    
    def init3():
        line8.set_data([],[])
        return line8,
    
    tracex , tracey = [] , []
    def animate3(i):
        tracex.append(x2[i])
        tracey.append(y2[i])
        line8.set_data(tracex , tracey)
        
        if i == len(theta_values)-1:
            tracex.clear()
            tracey.clear()
    
        return line8,
    
    fig3.canvas.manager.window.move(430,0)
    ani3 = animation.FuncAnimation(fig3, animate3,np.arange(1, len(theta_values)),
                                  interval=1, blit=True, init_func=init3 )
    
    
    plt.show()

except:
    print('Try again please !!...')
