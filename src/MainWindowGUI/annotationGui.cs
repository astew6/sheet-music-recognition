using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Numerics;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Windows.Forms.LinkLabel;

namespace MainWindowGUI
{
    public partial class annotationGui : Form
    {

        private Image originalImage;
        private float zoomFactor = 1.0f;
        private bool isDrawing = false;
        
        private List<Music_Component> musicComponents = new List<Music_Component> { };
        private Music_Component currentComponent;
        bool started = false;
        private Rectangle overlayRect;

        private bool clicked;

        public annotationGui()
        {
            InitializeComponent();
            customInit();
            originalImage = image.Image;

            overlayRect = new Rectangle(0, 0, image.Width, image.Height);
            image.MouseClick += image_MouseClick;
            image.Paint += image_Paint;
        }

        private void image_Paint(object? sender, PaintEventArgs e)
        {
            using (Pen pen = new Pen(Color.Red, 2))
            {
                e.Graphics.DrawRectangle(pen, overlayRect);
            }
        }

        private void image_MouseClick(object? sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left && isDrawing)
            {
                if (!started)
                {
                    currentComponent.setStartPoint(e.Location);
                    started = true;
                } else
                {
                    currentComponent.setEndPoint(e.Location);
                    started = false;
                    // rectangle has been set, just need to save it now
                    musicComponents.Add(currentComponent);
                    isDrawing = false;

                }
            }
        }

        private void annotationGui_Load(object sender, EventArgs e)
        {

        }

        private void SaveButton_Click(object sender, EventArgs e)
        {
            string filePath = "output.txt";

            List<string> lines = new List<string>();
            
            // Writes each element as a new line
            foreach (Music_Component i in musicComponents)
            {
                lines.Add(i.ToString());
            }
            
            File.WriteAllLines(filePath, lines);
            Console.WriteLine("List exported to " + filePath);
            this.DialogResult = DialogResult.OK;
            this.Close();
        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {

        }

        private void ApplyZoom(float factor)
        {
            zoomFactor *= factor;

            int newWidth = (int)(originalImage.Width * zoomFactor);
            int newHeight = (int)(originalImage.Height * zoomFactor);

            image.Size = new Size(newWidth, newHeight);
        }

        private void Zoom_In_Click(object sender, EventArgs e)
        {
            ApplyZoom(1.1f);
        }

        private void Zoom_Out_Click(object sender, EventArgs e)
        {
            ApplyZoom(0.9f);
        }

        private void Identification_Button_Click(object sender, EventArgs e)
        {
            this.isDrawing = !this.isDrawing;
            if (this.isDrawing == true)
            {
                currentComponent = new Music_Component();
            }
        }
    }
}
