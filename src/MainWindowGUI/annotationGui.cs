using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace MainWindowGUI
{
    public partial class annotationGui : Form
    {

        private Image originalImage;
        private float zoomFactor = 1.0f;
        private const float ZoomStep = 0.1f;

        public annotationGui()
        {
            InitializeComponent();
            customInit();
            originalImage = image.Image;
        }

        private void annotationGui_Load(object sender, EventArgs e)
        {

        }

        private void SaveButton_Click(object sender, EventArgs e)
        {
            this.DialogResult = DialogResult.OK;
            this.Close();
        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {

        }

        private void ApplyZoom()
        {
            if (originalImage == null) return;

            int newWidth = (int)(originalImage.Width * zoomFactor);
            int newHeight = (int)(originalImage.Height * zoomFactor);

            Bitmap bmp = new Bitmap(originalImage, newWidth, newHeight);
            image.Image = bmp;
        }

        private void Zoom_In_Click(object sender, EventArgs e)
        {
            zoomFactor += ZoomStep;
            ApplyZoom();
        }

        private void Zoom_Out_Click(object sender, EventArgs e)
        {
            if (zoomFactor > ZoomStep)
                zoomFactor -= ZoomStep;

            ApplyZoom();
        }
    }
}
