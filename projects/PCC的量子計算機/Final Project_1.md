�D�ءG�[���{�����欰
-----------------
�s�@�G���|�ġB�L���ʡB�笥�¡B���ߥ�
-----------------
�����G
���{���i�H���ϥΪ̧��ܪ�l����P��{���Ѽƨ��[���{�����欰

���w�q���
�������G��ODE���Ӥ@��ODE
deriv_1 = x���@���L��
deriv_2 = X���G���L��
[ deriv_1 , deriv_2 ]
x = [ , ]
x[0]��x���ȡAx[1]��x���@���L����

	 def deriv(x,t):
		deriv_1 = x[1]
		deriv_2 = epsilon*(1 - x[0]**2)*x[1] - x[0]
		return np.array([ deriv_1 , deriv_2 ])
	
����ODE
	 t = np.linspace(0.0,50.0,10000) 
	 xinit = np.array([1.0,0.0])
	 x = odeint(deriv,xinit,t)

���e�X��
	 ax1 = plt.subplot2grid((90,160), (0,0), colspan=160 , rowspan=20)
	 plt.subplots_adjust(bottom=0.1)
	 l, = plt.plot(t,x[:,0])
	 plt.axis([0, 50, -5, 5])
	 plt.title('van der Pol oscillator')
	 plt.xlabel('t')
	 plt.ylabel('x')

���]�w�Ʊ�

	 axcolor = 'lightgoldenrodyellow'

	 axxinit  = plt.axes([0.2, 0.40, 0.20, 0.02], axisbg=axcolor)
	 axdx_dtinit  = plt.axes([0.2, 0.35, 0.20, 0.02], axisbg=axcolor)
	 axepsilon = plt.axes([0.2, 0.30, 0.20, 0.02], axisbg=axcolor)

	 sxinit = Slider(axxinit, 'x init', 0.1, 5.0, valinit=xinit[0])
	 sdx_dtinit = Slider(axdx_dtinit, 'dx_dt init', 0.1, 5.0, valinit=xinit[1])
	 sepsilon = Slider(axepsilon, 'epsilon', 0.1, 3.0, valinit=epsilon)

������ƭȪ����
	def update(val):
		global epsilon,xinit 
    
		epsilon = sepsilon.val
		xinit[0] = sxinit.val
		xinit[1] = sdx_dtinit.val
		x = odeint(deriv,xinit,t)
		m.set_xdata(x[:,0])
		m.set_ydata(x[:,1])
		l.set_ydata(x[:,0])
		plt.draw()
	
�����{����s�ϧΪ����O(�h����update���)
	 sxinit.on_changed(update)
	 sdx_dtinit.on_changed(update)
	 sepsilon.on_changed(update)

���e�۹�
	 ax2 = plt.subplot2grid((90,160), (30,80), rowspan = 80,colspan = 80)
	 m, = plt.plot(x[:,0],x[:,1])
	 plt.axis([-6, 6, -6, 6])
	 plt.xlabel('x')
	 plt.ylabel('dx/dt')