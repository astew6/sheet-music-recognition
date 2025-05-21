using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Drawing.Imaging;
using System.Linq;
using System.Reflection.Metadata;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

using System.Runtime.InteropServices;


namespace MainWindowGUI
{
    public partial class imageEditor : Form
    {
        private Image originalImage;
        public imageEditor()
        {
            InitializeComponent();
            customInit();
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
            catch { }
        }
        private void updateImageEdit()
        {
            try
            {
                int left = int.Parse(leftCropValue.Text);
                int right = int.Parse(rightCropValue.Text);
                int top = int.Parse(topCropValue.Text);
                int bottom = int.Parse(bottomCropValue.Text);
                int brightnessOffset = brightScrollBar.Value;

                Bitmap original = new Bitmap(originalImage);

                // ROTATE
                Bitmap rotatedBmp = new Bitmap(original.Width, original.Height);
                rotatedBmp.SetResolution(original.HorizontalResolution, original.VerticalResolution);

                using (Graphics g = Graphics.FromImage(rotatedBmp))
                {
                    g.TranslateTransform(original.Width / 2f, original.Height / 2f);
                    g.RotateTransform(rotationScrollBar.Value);
                    g.TranslateTransform(-original.Width / 2f, -original.Height / 2f);
                    g.DrawImage(original, new Point(0, 0));
                }

                Rectangle cropRect = new Rectangle(
                    left,
                    top,
                    rotatedBmp.Width - left - right,
                    rotatedBmp.Height - top - bottom
                );

                Bitmap cropped = rotatedBmp.Clone(cropRect, rotatedBmp.PixelFormat);

                // BRIGHTNESS — optimized version
                Bitmap adjusted = new Bitmap(cropped.Width, cropped.Height, PixelFormat.Format24bppRgb);
                Rectangle rect = new Rectangle(0, 0, cropped.Width, cropped.Height);

                BitmapData srcData = cropped.LockBits(rect, ImageLockMode.ReadOnly, PixelFormat.Format24bppRgb);
                BitmapData dstData = adjusted.LockBits(rect, ImageLockMode.WriteOnly, PixelFormat.Format24bppRgb);

                int stride = srcData.Stride;
                unsafe
                {
                    byte* srcPtr = (byte*)srcData.Scan0;
                    byte* dstPtr = (byte*)dstData.Scan0;

                    for (int y = 0; y < cropped.Height; y++)
                    {
                        for (int x = 0; x < cropped.Width * 3; x++) // 3 bytes per pixel (BGR)
                        {
                            int val = srcPtr[y * stride + x] + brightnessOffset;
                            dstPtr[y * stride + x] = (byte)Math.Max(0, Math.Min(255, val));
                        }
                    }
                }

                cropped.UnlockBits(srcData);
                adjusted.UnlockBits(dstData);

                image.Image = adjusted;

                // Cleanup
                original.Dispose();
                rotatedBmp.Dispose();
                cropped.Dispose();
            }
            catch
            {
                // Optional: error logging
            }
        }



        private void rotateRightButton_Click(object sender, EventArgs e)
        {
            try
            {
                rotationScrollBar.Value += 90;
                rotationAngle.Text = $"{int.Parse(rotationAngle.Text) + 90}";
                updateImageEdit();
            }
            catch { }
        }

        private void rotateLeftButton_Click(object sender, EventArgs e)
        {
            {
                try
                {
                    rotationScrollBar.Value -= 90;
                    rotationAngle.Text = $"{int.Parse(rotationAngle.Text) - 90}";
                    updateImageEdit();
                }
                catch { }
            }
        }

        private void hScrollBar2_Scroll(object sender, ScrollEventArgs e)
        {
            updateImageEdit();
            brightnessValue.Text = brightScrollBar.Value.ToString();
        }

        private void brightnessValue_TextChanged(object sender, EventArgs e)
        {
            brightScrollBar.Value = int.Parse(brightnessValue.Text);
            updateImageEdit();
        }
    }
}
