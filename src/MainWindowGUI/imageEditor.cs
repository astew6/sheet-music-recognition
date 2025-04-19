using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Drawing.Text;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;


namespace MainWindowGUI
{
    public partial class imageEditor : Form
    {
        private Image originalImage = Image.FromFile(Program.app.inputPath);
        public imageEditor()
        {
            InitializeComponent();
        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {

        }

        private void topCropValue_TextChanged(object sender, EventArgs e)
        {
            try
            {
                Bitmap original = new Bitmap(originalImage); //gets the original image

                Rectangle cropRect = new Rectangle(0 + int.Parse(leftCropValue.Text), int.Parse(topCropValue.Text), original.Width - int.Parse(leftCropValue.Text) - int.Parse(rightCropValue.Text), original.Height - int.Parse(topCropValue.Text) - int.Parse(bottomCropValue.Text)); //creates a rectangle the size and location of the newly cropped image taking into account all the other cropping values
                Bitmap cropped = original.Clone(cropRect, original.PixelFormat); //creates the newly cropped image
                image.Image = cropped; //sets the image frame to display the cropped image
                original.Dispose();
            }
            catch { }
        }

        private void imageEditor_Load(object sender, EventArgs e)
        {

        }

        private void saveButton_Click(object sender, EventArgs e)
        {
            this.DialogResult = DialogResult.OK;
            this.Close();
        }

        private void leftCropValue_TextChanged(object sender, EventArgs e)
        {
            try
            {
                int cropSize = int.Parse(leftCropValue.Text); //gets the crop size of the image from the text field
                Bitmap original = new Bitmap(originalImage); //gets the original image

                Rectangle cropRect = new Rectangle(0 + int.Parse(leftCropValue.Text), int.Parse(topCropValue.Text), original.Width - int.Parse(leftCropValue.Text) - int.Parse(rightCropValue.Text), original.Height - int.Parse(topCropValue.Text) - int.Parse(bottomCropValue.Text)); //creates a rectangle the size and location of the newly cropped image taking into account all the other cropping values
                Bitmap cropped = original.Clone(cropRect, original.PixelFormat); //creates the newly cropped image
                image.Image = cropped; //sets the image frame to display the cropped image
                original.Dispose();
            }
            catch { }
        }

        private void bottomCropValue_TextChanged(object sender, EventArgs e)
        {
            try
            {
                int cropSize = int.Parse(bottomCropValue.Text); //gets the crop size of the image from the text field
                Bitmap original = new Bitmap(originalImage); //gets the original image

                Rectangle cropRect = new Rectangle(0 + int.Parse(leftCropValue.Text), int.Parse(topCropValue.Text), original.Width - int.Parse(leftCropValue.Text) - int.Parse(rightCropValue.Text), original.Height - int.Parse(topCropValue.Text) - int.Parse(bottomCropValue.Text)); //creates a rectangle the size and location of the newly cropped image taking into account all the other cropping values
                Bitmap cropped = original.Clone(cropRect, original.PixelFormat); //creates the newly cropped image
                image.Image = cropped; //sets the image frame to display the cropped image
                original.Dispose();
            }
            catch { }
        }

        private void rightCropValue_TextChanged(object sender, EventArgs e)
        {
            try
            {
                int cropSize = int.Parse(rightCropValue.Text); //gets the crop size of the image from the text field
                Bitmap original = new Bitmap(originalImage); //gets the original image

                Rectangle cropRect = new Rectangle(0 + int.Parse(leftCropValue.Text), int.Parse(topCropValue.Text), original.Width - int.Parse(leftCropValue.Text) - int.Parse(rightCropValue.Text), original.Height - int.Parse(topCropValue.Text) - int.Parse(bottomCropValue.Text)); //creates a rectangle the size and location of the newly cropped image taking into account all the other cropping values
                Bitmap cropped = original.Clone(cropRect, original.PixelFormat); //creates the newly cropped image
                image.Image = cropped; //sets the image frame to display the cropped image
                original.Dispose();
            }
            catch { }
        }
    }
}
