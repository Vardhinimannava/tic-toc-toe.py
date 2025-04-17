{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "c02b2754-082f-4220-bddc-5a023b62e415",
   "metadata": {},
   "outputs": [],
   "source": [
    "from tkinter import *\n",
    "from tkinter.ttk import *\n",
    "\n",
    "from time import strftime\n",
    "\n",
    "root = Tk()\n",
    "root.title('Clock')\n",
    "\n",
    "def time():\n",
    "\tstring = strftime('%H:%M:%S %p')\n",
    "\tlbl.config(text=string)\n",
    "\tlbl.after(1000, time)\n",
    "\n",
    "lbl = Label(root, font=('calibri', 40, 'bold'),\n",
    "\t\t\tbackground='white',\n",
    "\t\t\tforeground='black')\n",
    "\n",
    "lbl.pack(anchor='center')\n",
    "time()\n",
    "\n",
    "mainloop()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d1787927-d006-4f3d-9649-1ae7fc224f83",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
