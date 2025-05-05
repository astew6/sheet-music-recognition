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
            image = new PictureBox();
            Zoom_In = new Button();
            Zoom_Out = new Button();
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
            // image
            // 
            image.Location = new Point(215, 12);
            image.Name = "image";
            image.Size = new Size(452, 567);
            image.SizeMode = PictureBoxSizeMode.Zoom;
            image.TabIndex = 1;
            image.TabStop = false;
            image.Click += pictureBox1_Click;
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
            // annotationGui
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(686, 603);
            Controls.Add(Zoom_Out);
            Controls.Add(Zoom_In);
            Controls.Add(image);
            Controls.Add(SaveButton);
            Name = "annotationGui";
            Text = "annotationGui";
            Load += annotationGui_Load;
            ((System.ComponentModel.ISupportInitialize)image).EndInit();
            ResumeLayout(false);
        }

        private void customInit()
        {
            image.Image = Image.FromFile(Program.app.inputPath);
        }

        #endregion
        private Button SaveButton;
        private PictureBox image;
        private Button Zoom_In;
        private Button Zoom_Out;
    }
}