using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Reflection.Metadata;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace MainWindowGUI
{
    public partial class imageEditor : Form
    {
        private Image originalImage;
        public imageEditor()
        {
            InitializeComponent();
            originalImage = image.Image;
        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {

        }

        private void topCropValue_TextChanged(object sender, EventArgs e)
        {
            updateImageEdit();
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
            updateImageEdit();
        }

        private void bottomCropValue_TextChanged(object sender, EventArgs e)
        {
            updateImageEdit();
        }

        private void rightCropValue_TextChanged(object sender, EventArgs e)
        {
            updateImageEdit();
        }

        private void hScrollBar1_Scroll(object sender, ScrollEventArgs e)
        {
            updateImageEdit();
            rotationAngle.Text = rotationScrollBar.Value.ToString();
        }

        private void rotationAngle_TextChanged(object sender, EventArgs e)
        {
            try
            {
                rotationScrollBar.Value = int.Parse(rotationAngle.Text);
                updateImageEdit();
            }
            catch {}
        }
        private void updateImageEdit()
        {
            try
            {
                // Get crop values
                int left = int.Parse(leftCropValue.Text);
                int right = int.Parse(rightCropValue.Text);
                int top = int.Parse(topCropValue.Text);
                int bottom = int.Parse(bottomCropValue.Text);

                // Clone original image
                Bitmap original = new Bitmap(originalImage);

                // Create a new bitmap for rotation (size will match the original)
                Bitmap rotatedBmp = new Bitmap(original.Width, original.Height);
                rotatedBmp.SetResolution(original.HorizontalResolution, original.VerticalResolution);

                using (Graphics g = Graphics.FromImage(rotatedBmp))
                {
                    g.TranslateTransform(original.Width / 2f, original.Height / 2f);
                    g.RotateTransform(rotationScrollBar.Value);
                    g.TranslateTransform(-original.Width / 2f, -original.Height / 2f);

                    g.DrawImage(original, new Point(0, 0));
                }

                // Define crop rectangle based on rotated image
                Rectangle cropRect = new Rectangle(
                    left,
                    top,
                    rotatedBmp.Width - left - right,
                    rotatedBmp.Height - top - bottom
                );

                // Crop the rotated image
                Bitmap cropped = rotatedBmp.Clone(cropRect, rotatedBmp.PixelFormat);

                // Display final result
                image.Image = cropped;

                // Clean up
                rotatedBmp.Dispose();
                original.Dispose();
            }
            catch
            {
                // optional: log errors
            }
        }


    }
}
