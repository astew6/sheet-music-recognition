using System.Windows.Forms;

namespace MainWindowGUI
{
    partial class annotationGui
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            SaveButton = new Button();
            Zoom_In = new Button();
            Zoom_Out = new Button();
            image = new PictureBox();
            Identification_Button = new Button();
            ((System.ComponentModel.ISupportInitialize)image).BeginInit();
            SuspendLayout();
            // 
            // SaveButton
            // 
            SaveButton.Location = new Point(12, 537);
            SaveButton.Name = "SaveButton";
            SaveButton.Size = new Size(135, 54);
            SaveButton.TabIndex = 0;
            SaveButton.Text = "Save";
            SaveButton.UseVisualStyleBackColor = true;
            SaveButton.Click += SaveButton_Click;
            // 
            // Zoom_In
            // 
            Zoom_In.Location = new Point(12, 458);
            Zoom_In.Name = "Zoom_In";
            Zoom_In.Size = new Size(135, 54);
            Zoom_In.TabIndex = 2;
            Zoom_In.Text = "Zoom In";
            Zoom_In.UseVisualStyleBackColor = true;
            Zoom_In.Click += Zoom_In_Click;
            // 
            // Zoom_Out
            // 
            Zoom_Out.Location = new Point(12, 385);
            Zoom_Out.Name = "Zoom_Out";
            Zoom_Out.Size = new Size(135, 54);
            Zoom_Out.TabIndex = 3;
            Zoom_Out.Text = "Zoom Out";
            Zoom_Out.UseVisualStyleBackColor = true;
            Zoom_Out.Click += Zoom_Out_Click;
            // 
            // image
            // 
            image.Location = new Point(183, 12);
            image.Name = "image";
            image.Size = new Size(640, 626);
            image.SizeMode = PictureBoxSizeMode.Zoom;
            image.TabIndex = 1;
            image.TabStop = false;
            image.Click += pictureBox1_Click;
            // 
            // Identification_Button
            // 
            Identification_Button.Location = new Point(12, 309);
            Identification_Button.Name = "Identification_Button";
            Identification_Button.Size = new Size(135, 54);
            Identification_Button.TabIndex = 4;
            Identification_Button.Text = "Add Identification";
            Identification_Button.UseVisualStyleBackColor = true;
            Identification_Button.Click += Identification_Button_Click;
            // 
            // annotationGui
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(835, 650);
            ControlBox = false;
            Controls.Add(Identification_Button);
            Controls.Add(image);
            Controls.Add(Zoom_Out);
            Controls.Add(Zoom_In);
            Controls.Add(SaveButton);
            MaximizeBox = false;
            MinimizeBox = false;
            Name = "annotationGui";
            ShowInTaskbar = false;
            Text = "annotationGui";
            Load += annotationGui_Load;
            ((System.ComponentModel.ISupportInitialize)image).EndInit();
            ResumeLayout(false);
        }

        private void customInit()
        {
            image.Image = Image.FromFile(Program.app.inputPath);
        }

        private Size getImageFieldSize()
        {
            return image.Size;
        }

        #endregion
        private Button SaveButton;
        private Button Zoom_In;
        private Button Zoom_Out;
        private PictureBox image;
        private Button Identification_Button;
    }
}