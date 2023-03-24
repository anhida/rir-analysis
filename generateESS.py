import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

def expsweep(T, f1, f2, fs, debug=False):
    '''
    Generate exponential sine sweep (ESS) signal and its inverse.

    Input
    T           : sweep duration in (s)
    f1          : start frequency (Hz)
    f2          : end frequency (Hz)
    debug       : option to show plot of ESS signal and its inverse or not, default: False
    fs          : sampling frequency, default: 44100 (Hz)

    Output
    sweep       : ESS signal
    invsweep    : inverse filter of ESS
    '''

    # define parameter of ESS function
    w1 = 2 * np.pi * f1
    w2 = 2 * np.pi * f2
    t = np.linspace(0,(T*fs-1)/fs,T*fs)

    # create ESS signal
    K = T*w1/np.log(w2/w1)
    L = T/np.log(w2/w1)
    sweep = np.sin(K*(np.exp(t/L)-1))

    # create inverse filter
    G = np.exp(t/L)
    inv_sweep = sweep[::-1]/G

    # plot sweep signal and its inverse
    if debug == True:
        plt.figure()
        plt.subplot(2,1,1)
        plt.grid()
        plt.plot(t, sweep)
        plt.title('ESS signal')

        plt.subplot(2,1,2)
        plt.grid()
        plt.plot(t, inv_sweep)
        plt.title('Inverse filter of ESS signal')

        plt.show()

    write('sweep.wav', fs, sweep)
    write('inv_sweep.wav', fs, inv_sweep)

    return sweep, inv_sweep

if __name__ == '__main__':
    # define input of sweep function
    T = 10
    f1 = 125
    f2 = 4000
    fs = 48000
    debug = True

    sweep, invsweep = expsweep(T, f1, f2, fs, debug)
