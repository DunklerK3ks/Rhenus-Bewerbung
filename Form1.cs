using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace RhEnus
{
    public partial class Form1 : Form
    {
        private TimeSpan timeleft;
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void timer1_Tick(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void schiff_Tick(object sender, EventArgs e) # Der Timer in dieses Beispiel benannt als schiff_tick
        {
            timeleft = timeleft.Subtract(TimeSpan.FromSeconds(1)); # Hier das de Intervall eine Minute immer eine Zahl weniger wird
            label1.Text = timeleft.ToString(@"hh\:mm\:ss"); # Die Aktulisierung vom String
        }

        private void button1_Click(object sender, EventArgs e)
        {
            timeleft = new TimeSpan(0, 30, 0); # Die Start grundwerte
            label1.Text = timeleft.ToString(@"hh\:mm");
            schiff.Start(); #Der Timer startet
       }
    }
}
