import serial
import streamlit as st
from take_part import enable

def start():
    ser = None
    try:
        ser = serial.Serial(port='COM3', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE)
        if ser.is_open:
            st.write("port enabled")
            print("Port is enabled")
            ser.write(b'\x02')
            ser.write(b'\x03')
            enable(ser)
        else:
            print("Failed to open port")
    except serial.SerialException as e:
        print(f"Error: could not open port 'COM3': {e}")

def end():
    ser = serial.Serial(port='COM3')
    ser.write(b'\x05')
    st.write("port closed")
    ser.close()