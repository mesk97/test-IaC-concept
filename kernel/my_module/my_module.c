#define MODULE
#include <linux/module.h>
#include <linux/init.h>
#include <linux/kernel.h>

MODULE_LICENSE("GPLv3");
MODULE_AUTHOR("Konstantin Pakulin");
MODULE_DESCRIPTION("Simplest Linux module");
MODULE_VERSION("0.01");


int init_module(void){
	printk("Hello,World\n");
        return 0;
}

void cleanup_module(void){
	printk("Goodbye.\n");
}

