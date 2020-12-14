private void button1_Click(object sender, EventArgs e)
        {
            try//32λ
            {
                Microsoft.Win32.RegistryKey key;
                key = Microsoft.Win32.Registry.LocalMachine.CreateSubKey(@"SOFTWARE\MICROSOFT\.NETFramework\Security\TrustManager\PromptingLevel");

                key.SetValue("MyComputer", "Enabled");
                key.SetValue("LocalIntranet", "Enabled");
                key.SetValue("Internet", "Enabled");
                key.SetValue("TrustedSites", "Enabled");
                key.SetValue("UntrustedSites", "Enabled");
                key.Close();
                MessageBox.Show("Security Reg Done!");
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            try//64λ
            {
                Microsoft.Win32.RegistryKey key;
                key = Microsoft.Win32.Registry.LocalMachine.CreateSubKey(@"SOFTWARE\Wow6432Node\MICROSOFT\.NETFramework\Security\TrustManager\PromptingLevel");

                key.SetValue("MyComputer", "Enabled");
                key.SetValue("LocalIntranet", "Enabled");
                key.SetValue("Internet", "Enabled");
                key.SetValue("TrustedSites", "Enabled");
                key.SetValue("UntrustedSites", "Enabled");
                key.Close();
                MessageBox.Show("Security Reg Done!");
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }
