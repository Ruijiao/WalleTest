package test.com.walletest;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.Toast;

import com.meituan.android.walle.WalleChannelReader;


public class MainActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        findViewById(R.id.button).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // 如果没有使用PackerNg打包添加渠道，默认返回的是""
                // com.mcxiaoke.packer.helper.PackerNg
                String channel = WalleChannelReader.getChannel(MainActivity.this.getApplicationContext());
//                ChannelInfo channelInfo= WalleChannelReader.getChannelInfo(MainActivity.this.getApplicationContext());
//                String channel = "111";
//                if (channelInfo != null) {
//                    channel = channelInfo.getChannel();
//                }
                Toast.makeText(MainActivity.this,channel,Toast.LENGTH_SHORT).show();
                // 或者使用 PackerNg.getMarket(Context,defaultValue)
                // 之后就可以使用了，比如友盟可以这样设置
//                AnalyticsConfig.setChannel(market)
            }
        });
    }
}
