namespace MainWindowGUI
{
    partial class imageEditor
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(imageEditor));
            pictureBox1 = new PictureBox();
            label1 = new Label();
            width = new TextBox();
            height = new TextBox();
            label2 = new Label();
            hScrollBar1 = new HScrollBar();
            hScrollBar2 = new HScrollBar();
            label3 = new Label();
            hScrollBar3 = new HScrollBar();
            label4 = new Label();
            saveButton = new Button();
            ((System.ComponentModel.ISupportInitialize)pictureBox1).BeginInit();
            SuspendLayout();
            // 
            // pictureBox1
            // 
            pictureBox1.Image = (Image)resources.GetObject("pictureBox1.Image");
            pictureBox1.Location = new Point(130, 12);
            pictureBox1.Name = "pictureBox1";
            pictureBox1.Size = new Size(561, 645);
            pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage;
            pictureBox1.TabIndex = 0;
            pictureBox1.TabStop = false;
            pictureBox1.Click += pictureBox1_Click;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Font = new Font("Yu Gothic", 20F);
            label1.Location = new Point(12, 9);
            label1.Name = "label1";
            label1.Size = new Size(74, 35);
            label1.TabIndex = 1;
            label1.Text = "Crop";
            // 
            // width
            // 
            width.Location = new Point(12, 47);
            width.Name = "width";
            width.Size = new Size(100, 23);
            width.TabIndex = 2;
            width.TextChanged += textBox1_TextChanged;
            // 
            // height
            // 
            height.Location = new Point(12, 76);
            height.Name = "height";
            height.Size = new Size(100, 23);
            height.TabIndex = 3;
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Font = new Font("Yu Gothic", 20F);
            label2.Location = new Point(12, 102);
            label2.Name = "label2";
            label2.Size = new Size(98, 35);
            label2.TabIndex = 4;
            label2.Text = "Rotate";
            // 
            // hScrollBar1
            // 
            hScrollBar1.LargeChange = 1;
            hScrollBar1.Location = new Point(12, 137);
            hScrollBar1.Name = "hScrollBar1";
            hScrollBar1.Size = new Size(100, 17);
            hScrollBar1.TabIndex = 5;
            hScrollBar1.Value = 50;
            // 
            // hScrollBar2
            // 
            hScrollBar2.LargeChange = 1;
            hScrollBar2.Location = new Point(12, 189);
            hScrollBar2.Name = "hScrollBar2";
            hScrollBar2.Size = new Size(100, 17);
            hScrollBar2.TabIndex = 7;
            hScrollBar2.Value = 50;
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Font = new Font("Yu Gothic", 20F);
            label3.Location = new Point(12, 154);
            label3.Name = "label3";
            label3.Size = new Size(91, 35);
            label3.TabIndex = 6;
            label3.Text = "Bright";
            // 
            // hScrollBar3
            // 
            hScrollBar3.LargeChange = 1;
            hScrollBar3.Location = new Point(12, 241);
            hScrollBar3.Name = "hScrollBar3";
            hScrollBar3.Size = new Size(100, 17);
            hScrollBar3.TabIndex = 9;
            hScrollBar3.Value = 50;
            // 
            // label4
            // 
            label4.AutoSize = true;
            label4.Font = new Font("Yu Gothic", 20F);
            label4.Location = new Point(12, 206);
            label4.Name = "label4";
            label4.Size = new Size(74, 35);
            label4.TabIndex = 8;
            label4.Text = "Cont";
            // 
            // saveButton
            // 
            saveButton.Location = new Point(11, 610);
            saveButton.Name = "saveButton";
            saveButton.Size = new Size(113, 47);
            saveButton.TabIndex = 10;
            saveButton.Text = "Save";
            saveButton.UseVisualStyleBackColor = true;
            saveButton.Click += saveButton_Click;
            // 
            // imageEditor
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(703, 669);
            ControlBox = false;
            Controls.Add(saveButton);
            Controls.Add(hScrollBar3);
            Controls.Add(label4);
            Controls.Add(hScrollBar2);
            Controls.Add(label3);
            Controls.Add(hScrollBar1);
            Controls.Add(label2);
            Controls.Add(height);
            Controls.Add(width);
            Controls.Add(label1);
            Controls.Add(pictureBox1);
            MaximizeBox = false;
            MinimizeBox = false;
            Name = "imageEditor";
            ShowInTaskbar = false;
            Text = "imageEditor";
            Load += imageEditor_Load;
            ((System.ComponentModel.ISupportInitialize)pictureBox1).EndInit();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private PictureBox pictureBox1;
        private Label label1;
        private TextBox width;
        private TextBox height;
        private Label label2;
        private HScrollBar hScrollBar1;
        private HScrollBar hScrollBar2;
        private Label label3;
        private HScrollBar hScrollBar3;
        private Label label4;
        private Button saveButton;
    }
}